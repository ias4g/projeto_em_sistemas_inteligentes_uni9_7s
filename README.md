# Projeto em Sistemas Inteligentes - Travel Assistant

Este projeto consiste em uma aplicação de assistente de viagens que utiliza inteligência artificial para criar roteiros personalizados. O sistema é composto por um backend em Python/Django e um frontend em React.

## Estrutura do Projeto
```
projeto_em_sistemas_inteligentes/
├── travel_assistant_back/    # Backend em Python/Django
└── travel_assistant_front/   # Frontend em React
```

## Pré-requisitos Gerais
- Git
- Python 3.10 ou superior
- Node.js 16.x ou superior
- npm ou yarn
- Chave de API do Google (para o modelo Gemini)

## Configuração do Backend (travel_assistant_back)

### 1. Acesse a pasta do backend
```bash
cd travel_assistant_back
```

### 2. Crie e ative o ambiente virtual
```bash
# No Linux/Mac
python3 -m venv venv
source venv/bin/activate

# No Windows
python3 -m venv venv
.\venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente
Crie um arquivo `.env` na pasta `travel_assistant_back`:
```bash
GOOGLE_API_KEY=sua_chave_api_aqui
```

### 5. Inicie o servidor backend
```bash
python app.py
```
O servidor estará disponível em `http://localhost:8000`

## Configuração do Frontend (travel_assistant_front)

### 1. Acesse a pasta do frontend
```bash
cd travel_assistant_front
```

### 2. Instale as dependências
```bash
npm install
# ou
yarn install
```

### 3. Configure as variáveis de ambiente
Crie um arquivo `.env` na pasta `travel_assistant_front`:
```bash
REACT_APP_API_URL=http://localhost:8000
```

### 4. Inicie o servidor de desenvolvimento
```bash
npm start
# ou
yarn start
```
A aplicação estará disponível em `http://localhost:3000`

## Funcionalidades Principais

### Backend
- Geração de roteiros personalizados
- Busca inteligente na Wikipedia e web
- API RESTful com documentação Swagger
- Armazenamento em banco de dados vetorial

### Frontend
- Interface moderna e responsiva
- Visualização de roteiros
- Interação com o assistente de IA
- Personalização de preferências

## Solução de Problemas

### Backend
1. **Erro de Conexão com a API do Google**
   - Verifique se a chave API está correta no arquivo `.env`
   - Confirme se a chave tem permissões para o Gemini

2. **Erro ao Iniciar o Servidor**
   - Verifique se todas as dependências foram instaladas
   - Confirme se o ambiente virtual está ativado
   - Verifique se a porta 8000 está disponível

### Frontend
1. **Erro de Conexão com o Backend**
   - Verifique se o backend está rodando
   - Confirme se a URL da API está correta no arquivo `.env`
   - Verifique se não há bloqueio de CORS

2. **Erro ao Instalar Dependências**
   - Limpe o cache do npm/yarn
   - Delete a pasta node_modules e package-lock.json
   - Execute npm install ou yarn install novamente

## Licença
Este projeto está sob a licença MIT.