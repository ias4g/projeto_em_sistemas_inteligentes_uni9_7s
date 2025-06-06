import google.generativeai as genai
from config.settings import GEMINI_API_KEY, GEMINI_MODEL, GEMINI_CONFIG

class GeminiClient:
    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError("GOOGLE_API_KEY não encontrada nas variáveis de ambiente")
        
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(GEMINI_MODEL)

    def generate_content(self, prompt, system_instruction=None):
        try:
            if system_instruction:
                response = self.model.generate_content(
                    contents=prompt,
                    generation_config=GEMINI_CONFIG,
                    safety_settings={"HARASSMENT": "block_none"},
                    system_instruction=system_instruction
                )
            else:
                response = self.model.generate_content(
                    contents=prompt,
                    generation_config=GEMINI_CONFIG,
                    safety_settings={"HARASSMENT": "block_none"}
                )
            
            return response.text
                
        except Exception as e:
            raise Exception(f"Erro na requisição à API do Gemini: {str(e)}")

def get_gemini_client():
    return GeminiClient() 