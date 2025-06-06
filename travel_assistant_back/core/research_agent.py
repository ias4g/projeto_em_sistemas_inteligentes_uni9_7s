from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate
import os
import requests
from bs4 import BeautifulSoup
from services.gemini_client import get_gemini_client

class ResearchAgent:
    def __init__(self):
        self.gemini = get_gemini_client()
        # Configurando o USER_AGENT para as requisições web
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        # Definindo o prompt template diretamente
        self.prompt_template = """
        Você é um assistente de pesquisa especializado em viagens. Sua tarefa é pesquisar informações sobre eventos, destinos turísticos e preços de passagens.

        Regras importantes:
        1. Sempre siga o formato exato abaixo
        2. Use a ferramenta Wikipedia para pesquisar informações sobre destinos
        3. Espere a observação antes de tomar a próxima ação
        4. Não forneça respostas finais até ter todas as informações necessárias
        5. Pesquise eventos específicos para a data solicitada
        6. Inclua preços de passagens quando disponíveis
        7. Seja detalhado e específico nas informações

        Use o seguinte formato:

        Question: {input}
        Thought: (pense no que precisa pesquisar)
        Action: (escolha uma ação: [pesquisar_wikipedia, pesquisar_web])
        Action Input: (termo de pesquisa)
        Observation: (resultado da pesquisa)
        Thought: (analise o resultado e decida o próximo passo)
        ... (repita até ter todas as informações)
        Thought: agora tenho todas as informações necessárias
        Final Answer: (resposta completa e detalhada)

        Question: {input}
        Thought:{agent_scratchpad}
        """

    def _search_wikipedia(self, query):
        try:
            import wikipedia
            wikipedia.set_lang("pt")
            results = wikipedia.search(query, results=3)
            content = []
            for result in results:
                try:
                    page = wikipedia.page(result)
                    content.append(f"{page.title}:\n{page.summary}")
                except:
                    continue
            return "\n\n".join(content)
        except Exception as e:
            print(f"Erro na pesquisa Wikipedia: {str(e)}")
            return ""

    def _search_web(self, query):
        try:
            # Pesquisa no Google (usando DuckDuckGo como proxy)
            url = f"https://html.duckduckgo.com/html/?q={query}"
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            results = []
            for result in soup.find_all('div', class_='result'):
                title = result.find('h2')
                snippet = result.find('a', class_='result__snippet')
                if title and snippet:
                    results.append(f"{title.text}: {snippet.text}")
            return "\n".join(results[:5])  # Retorna os 5 primeiros resultados
        except Exception as e:
            print(f"Erro na pesquisa web: {str(e)}")
            return ""

    def research(self, query):
        try:
            # Primeiro, faz uma pesquisa na web
            web_results = self._search_web(query)
            wiki_results = self._search_wikipedia(query)
            
            # Prepara o prompt com os resultados das pesquisas
            prompt = f"""
            {self.prompt_template}
            
            Question: {query}
            
            Informações da web:
            {web_results}
            
            Informações da Wikipedia:
            {wiki_results}
            
            Por favor, analise estas informações e forneça uma resposta completa.
            """
            
            # Usa o Gemini para gerar a resposta
            response = self.gemini.generate_content(prompt)
            
            return response
        except Exception as e:
            print(f"Erro durante a pesquisa: {str(e)}")
            return """
            Desculpe, ocorreu um erro durante a pesquisa. Por favor, tente novamente com uma consulta mais específica.
            """ 