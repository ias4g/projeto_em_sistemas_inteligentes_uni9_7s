import { StatusProps } from '../types';
import { COLORS, MESSAGES } from '../constants';
import { XIcon } from "@phosphor-icons/react";

export const Status = ({ isLoading, savedItineraries, onSelectItinerary, onDeleteItinerary }: StatusProps) => (
  <div className={`space-y-6 flex-1 flex flex-col items-center rounded-md border ${COLORS.BORDER} px-2 py-3`}>
    {/* {isLoading && (
      <div className="flex items-center gap-2">
        <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-purple-600"></div>
        <span className="text-xs">{MESSAGES.GENERATING}</span>
      </div>
    )} */}
    
    {savedItineraries.length > 0 && (
      <div className="w-full mt-4">
        <h3 className="text-sm font-medium mb-2 ml-4">Roteiros Salvos</h3>
        <div className="space-y-2 overflow-y-auto">
          {savedItineraries.map((itinerary) => (
            <div key={itinerary.id} className="group relative p-2">
              <button
                onClick={() => onSelectItinerary(itinerary.content, itinerary.title)}
                className="w-full text-left p-2 rounded hover:bg-violet-500 transition-colors"
              >
                <div className="text-sm font-medium truncate">{itinerary.title}</div>
                <div className="text-xs text-gray-500 flex justify-between mt-2">
                  <span>{itinerary.date}</span>
                  <span className="hover:text-white">{itinerary.time}</span>
                </div>
              </button>
              <button
                onClick={(e) => {
                  e.stopPropagation();
                  onDeleteItinerary(itinerary.id);
                }}
                title='Excluir'
                className="absolute right-0 top-0 opacity-0 bg-violet-500 group-hover:opacity-100 transition-opacity p-1 hover:bg-red-500 rounded-full"
              >
                <XIcon className="size-4 text-gray-500 group-hover:text-white" weight="bold" />
              </button>
            </div>
          ))}
        </div>
        {isLoading && (
          <div className="flex items-center justify-center gap-2 mt-4">
            <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-purple-600"></div>
            <span className="text-xs">{MESSAGES.GENERATING}</span>
          </div>
        )}
      </div>
    )}
  </div>
); 