export interface ApiError {
  code?: string;
  response?: {
    status: number;
  };
}

export interface NetworkError extends ApiError {
  code: 'ERR_NETWORK';
}

export interface ServerError extends ApiError {
  response: {
    status: number;
  };
}

export type AppError = NetworkError | ServerError | ApiError; 