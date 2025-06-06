from pydantic import BaseModel, Field

class Query(BaseModel):
    question: str = Field(..., description="Pergunta ou solicitação do usuário sobre viagens")

class Response(BaseModel):
    response: str = Field(..., description="Resposta do assistente de viagens") 