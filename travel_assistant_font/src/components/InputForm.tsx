import { Textarea } from "./ui/textarea";
import { InputFormProps } from '../types';

export const InputForm = ({ input, handleInputChange, isLoading }: InputFormProps) => (
  <form>
    <Textarea
      placeholder="Inclua o prompt para a AI... (Ex: Faça para mim um roteiro de viagem para São Paulo na próxima semana)"
      className="resize-none p-4 leading-relaxed text-base"
      value={input}
      onChange={handleInputChange}
      disabled={isLoading}
    />
  </form>
); 