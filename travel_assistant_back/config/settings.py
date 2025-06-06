import os
from dotenv import load_dotenv

load_dotenv()

# Configurações da API
API_HOST = "0.0.0.0"
API_PORT = 8000
API_TITLE = "Travel Assistant API"

# Configurações do Gemini
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = "gemini-2.5-flash-preview-05-20"

# Configurações do CORS
CORS_ORIGINS = ["*"]
CORS_CREDENTIALS = True
CORS_METHODS = ["*"]
CORS_HEADERS = ["*"]

# Configurações do Gemini
GEMINI_CONFIG = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 10000
} 