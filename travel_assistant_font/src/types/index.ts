export interface StatusProps {
  completion: string;
  isLoading: boolean;
  savedItineraries: Array<{
    id: string;
    title: string;
    content: string;
    date: string;
    time: string;
  }>;
  onSelectItinerary: (content: string, title: string) => void;
  onDeleteItinerary: (id: string) => void;
}

export interface InputFormProps {
  input: string;
  handleInputChange: (e: React.ChangeEvent<HTMLTextAreaElement>) => void;
  isLoading: boolean;
}

export interface ResultProps {
  completion: string;
} 