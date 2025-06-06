import { Button } from "@/components/ui/button";
import { MagicWandIcon } from "@phosphor-icons/react";
import { ChangeEvent, FormEvent, useState, useEffect } from 'react';
import { api } from "./lib/axios";
import { Header } from './components/Header';
import { Status } from './components/Status';
import { InputForm } from './components/InputForm';
import { Result } from './components/Result';
import { API_ENDPOINTS, MESSAGES } from './constants';
import toast, { Toaster } from 'react-hot-toast';
import { AppError, NetworkError, ServerError } from './types/error';

interface SavedItinerary {
  id: string;
  title: string;
  content: string;
  date: string;
  time: string;
}

export function App() {
  const [input, setInput] = useState('');
  const [completion, setCompletion] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [savedItineraries, setSavedItineraries] = useState<SavedItinerary[]>([]);

  useEffect(() => {
    const loadSavedItineraries = () => {
      const saved = localStorage.getItem('itineraries');
      if (saved) {
        setSavedItineraries(JSON.parse(saved));
      }
    };

    loadSavedItineraries();
  }, []);

  const handleInputChange = (e: ChangeEvent<HTMLTextAreaElement>) => {
    setInput(e.target.value);
  };

  const handleError = (error: AppError) => {
    if (isNetworkError(error)) {
      toast.error(MESSAGES.NETWORK_ERROR, {
        duration: 4000,
        position: 'top-center',
      });
    } else if (isServerError(error)) {
      toast.error(MESSAGES.SERVER_ERROR, {
        duration: 4000,
        position: 'top-center',
      });
    } else {
      toast.error(MESSAGES.UNKNOWN_ERROR, {
        duration: 4000,
        position: 'top-center',
      });
    }

    setCompletion('');
  };

  const isNetworkError = (error: AppError): error is NetworkError => {
    return error.code === 'ERR_NETWORK';
  };

  const isServerError = (error: AppError): error is ServerError => {
    return Boolean(error.response?.status && error.response.status >= 500);
  };

  const saveItinerary = (content: string) => {
    const now = new Date();
    const newItinerary: SavedItinerary = {
      id: Date.now().toString(),
      title: input,
      content,
      date: now.toLocaleDateString('pt-BR'),
      time: now.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' })
    };
    const updatedItineraries = [...savedItineraries, newItinerary];
    setSavedItineraries(updatedItineraries);
    localStorage.setItem('itineraries', JSON.stringify(updatedItineraries));
  };

  const handleSelectItinerary = (content: string, title: string) => {
    setInput(title);
    setCompletion(content);
  };

  const handleDeleteItinerary = (id: string) => {
    const updatedItineraries = savedItineraries.filter(itinerary => itinerary.id !== id);
    setSavedItineraries(updatedItineraries);
    localStorage.setItem('itineraries', JSON.stringify(updatedItineraries));
  };

  const onSubmit = async (e: FormEvent) => {
    e.preventDefault();

    if (!input.trim()) {
      toast.error(MESSAGES.EMPTY_INPUT, {
        duration: 3000,
        position: 'top-center',
      });
      return;
    }
    
    setIsLoading(true);

    try {
      const response = await api.post(API_ENDPOINTS.ITINERARY, {
        question: input,
      }, {
        headers: {
          'Content-Type': 'application/json',
        },
      });
      const data = response.data.response;

      const itineraryContent = data.itinerary || data;
      setCompletion(itineraryContent);
      saveItinerary(itineraryContent);
      setInput('');

      toast.success(MESSAGES.SUCCESS, {
        duration: 3000,
        position: 'top-center',
      });

    } catch (err) {
      console.error(MESSAGES.ERROR, err);
      handleError(err as AppError);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col">
      <Toaster />
      <Header />

      <main className="flex-1 p-6 flex gap-6">
        <div className="flex flex-col flex-1 gap-4">
          <div className="grid grid-rows-1 gap-4 flex-1">
            <Result completion={completion} />
          </div>

          <InputForm
            input={input}
            handleInputChange={handleInputChange}
            isLoading={isLoading}
          />
        </div>

        <aside className="w-64 space-y-4 flex flex-col justify-between">
          <Status
            completion={completion}
            isLoading={isLoading}
            savedItineraries={savedItineraries}
            onSelectItinerary={handleSelectItinerary}
            onDeleteItinerary={handleDeleteItinerary}
          />

          <Button
            variant="ghost"
            disabled={isLoading || !input.trim()}
            onClick={onSubmit}
            className="w-full min-h-[80px] gap-2"
            type="submit"
          >
            {isLoading ? (
              <>
                <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white"></div>
                {MESSAGES.GENERATING}
              </>
            ):(
              <>
                Gerar roteiro
                <MagicWandIcon className="size-4 ml-2" weight="bold" />
              </>
            )}
          </Button>
        </aside>
      </main>
    </div>
  );
}