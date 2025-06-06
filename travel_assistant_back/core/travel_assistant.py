from .research_agent import ResearchAgent
from .document_loader import DocumentLoader
from .supervisor_agent import SupervisorAgent

class TravelAssistant:
    def __init__(self):
        self.research_agent = ResearchAgent()
        self.document_loader = DocumentLoader()
        self.supervisor_agent = SupervisorAgent()

    def get_response(self, query):
        web_context = self.research_agent.research(query)
        relevant_documents = self.document_loader.get_relevant_docs(query)
        response = self.supervisor_agent.generate_itinerary(query, web_context, relevant_documents)
        return response 