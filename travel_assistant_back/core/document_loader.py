from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import bs4
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

class DocumentLoader:
    def __init__(self):
        self.vectorstore = None
        self._initialize_vectorstore()

    def _fetch_travel_blog_content(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.find('article') or soup.find('main') or soup.find('div', class_='content')
            return str(content) if content else ""
        except Exception as e:
            print(f"Erro ao buscar conteúdo de {url}: {str(e)}")
            return ""

    def _initialize_vectorstore(self):
        # Lista de fontes de dados sobre viagens
        sources = [
            "https://www.dicasdeviagem.com/brasil/",
            "https://www.viagensecaminhos.com/",
            "https://www.melhoresdestinos.com.br/"
        ]
        
        all_docs = []
        for source in sources:
            try:
                # Carrega o conteúdo da página
                loader = WebBaseLoader(
                    web_paths=(source,),
                    bs_kwargs=dict(
                        parse_only=bs4.SoupStrainer(
                            class_=(
                                "postcontentwrap",
                                "pagetitleloading background-imaged loading-dark",
                                "content",
                                "article"
                            )
                        )
                    ),
                )
                docs = loader.load()
                all_docs.extend(docs)
            except Exception as e:
                print(f"Erro ao carregar {source}: {str(e)}")
                continue

        if not all_docs:
            raise Exception("Não foi possível carregar nenhum documento")

        # Divide os documentos em chunks menores
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        splits = text_splitter.split_documents(all_docs)

        # Cria o vectorstore com embeddings do Gemini
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            task_type="retrieval_document"
        )
        
        # Remove o banco de dados existente se houver
        if os.path.exists("./chroma_db"):
            import shutil
            shutil.rmtree("./chroma_db")
        
        self.vectorstore = Chroma.from_documents(
            documents=splits,
            embedding=embeddings,
            persist_directory="./chroma_db"
        )

    def get_relevant_docs(self, query):
        try:
            if not self.vectorstore:
                self._initialize_vectorstore()
            
            retriever = self.vectorstore.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 3}
            )
            relevant_documents = retriever.invoke(query)
            return relevant_documents
        except Exception as e:
            print(f"Erro ao buscar documentos relevantes: {str(e)}")
            return [] 