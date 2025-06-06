from services.gemini_client import get_gemini_client

class SupervisorAgent:
    def __init__(self):
        self.gemini = get_gemini_client()
        self.prompt_template = """
        Você é um gerente de uma agência de viagens especializado em criar roteiros personalizados. 
        Sua tarefa é criar um roteiro de viagem completo e detalhado baseado nas informações fornecidas.

        Instruções:
        1. Analise cuidadosamente o contexto da pesquisa e os documentos relevantes
        2. Crie um roteiro detalhado incluindo:
           - Pontos turísticos principais
           - Atividades recomendadas
           - Opções de hospedagem
           - Restaurantes e gastronomia local
           - Eventos e festivais (se houver)
           - Dicas de transporte
           - Orçamento estimado
        3. Organize o roteiro por dias
        4. Inclua horários sugeridos
        5. Adicione dicas úteis e precauções
        6. Seja específico e realista

        Contexto da pesquisa: {webContext}
        Documentos relevantes: {relevant_documents}
        Consulta do usuário: {query}

        Por favor, forneça um roteiro completo e detalhado:
        """

    def generate_itinerary(self, query, web_context, relevant_documents):
        try:
            # Prepara os documentos relevantes para o prompt
            formatted_docs = "\n".join([doc.page_content for doc in relevant_documents])
            
            # Prepara o prompt completo
            prompt = self.prompt_template.format(
                webContext=web_context,
                relevant_documents=formatted_docs,
                query=query
            )
            
            # Gera a resposta usando o Gemini
            response = self.gemini.generate_content(prompt)
            return response
            
        except Exception as e:
            print(f"Erro ao gerar roteiro: {str(e)}")
            return "Desculpe, ocorreu um erro ao gerar o roteiro. Por favor, tente novamente." 