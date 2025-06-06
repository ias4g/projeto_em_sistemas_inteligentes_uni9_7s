export const API_ENDPOINTS = {
  ITINERARY: 'itinerary'
} as const;

export const COLORS = {
  PRIMARY: '#7B52AB',
  BORDER: 'border-green-900/50'
} as const;

export const MESSAGES = {
  EMPTY_INPUT: 'Por favor, digite uma pergunta antes de executar.',
  GENERATING: 'Gerando roteiro...',
  SUCCESS: 'Roteiro gerado com sucesso!',
  NO_ITINERARY: 'Nenhum roteiro gerado',
  ERROR: 'Erro ao gerar roteiro:',
  ERROR_TITLE: 'Erro',
  SUCCESS_TITLE: 'Sucesso',
  NETWORK_ERROR: 'Erro de conexão. Verifique sua internet.',
  SERVER_ERROR: 'Erro no servidor. Tente novamente mais tarde.',
  UNKNOWN_ERROR: 'Ocorreu um erro inesperado.'
} as const; 