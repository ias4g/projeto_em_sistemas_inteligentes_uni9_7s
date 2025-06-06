import { Textarea } from "./ui/textarea";
import { ResultProps } from '../types';

export const Result = ({ completion }: ResultProps) => (
  <Textarea
    readOnly
    placeholder="Resultado gerado pela AI..."
    className="resize-none p-4 leading-relaxed text-base"
    value={completion || ''}
  />
); 