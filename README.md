Spotify ETL Project

Descrição

Este projeto realiza a extração de dados da API do Spotify, transformando e armazenando as informações em planilhas do Excel. O objetivo é coletar dados sobre artistas, álbuns e faixas, proporcionando uma análise detalhada das músicas disponíveis na plataforma.

Funcionalidades

Extração de dados da API do Spotify

Armazenamento de dados em arquivos JSON

Processamento e limpeza de dados

Exportação para planilhas do Excel

Estrutura do Repositório

📂 ETL
├── 📂 data
│   ├── 📂 raw            # Dados brutos extraídos da API
│   ├── 📂 processed      # Dados transformados e processados
├──  📂 scripts            # Códigos para extração, transformação e carregamento
│   ├── Extract.py        # Script de extração de dados
│   ├── Transform.py      # Script de transformação dos dados
│   ├── Load.py           # Script de carregamento dos dados
│── 📂 excel              # Dados tabulados em Excel
├── 📜 requirements.txt   # Dependências do projeto
├── 📜 README.md          # Documentação do projeto

Tecnologias Utilizadas

Linguagem: Python 3

Bibliotecas:

requests

pandas

openpyxl

sqlalchemy

psycopg2

dotenv

Como Executar

Clone o repositório:

git clone https://github.com/GustavoOliveira-jpg/ETL/ETL.git
cd Spotify_ETL

Crie um ambiente virtual e instale as dependências:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
pip install -r requirements.txt

Crie um arquivo .env com suas credenciais da API do Spotify:

CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret

Execute os scripts na seguinte ordem:

python scripts/Extract.py  # Extração dos dados
python scripts/Transform.py  # Transformação dos dados
python scripts/Load.py  # Carregamento dos dados

Referências

Documentação da API do Spotify

Vídeo Tutorial: Como Extrair Dados da API do Spotify

Dependências

Arquivo requirements.txt com as bibliotecas necessárias:

asttokens==3.0.0
certifi==2025.1.31
chardet==5.2.0
charset-normalizer==3.4.1
colorama==0.4.6
comm==0.2.2
debugpy==1.8.12
decorator==5.2.1
et_xmlfile==2.0.0
executing==2.2.0
greenlet==3.1.1
idna==3.10
ipykernel==6.29.5
ipython==9.0.0
ipython_pygments_lexers==1.1.1
jedi==0.19.2
jupyter_client==8.6.3
jupyter_core==5.7.2
matplotlib-inline==0.1.7
nest-asyncio==1.6.0
numpy==2.2.3
openpyxl==3.1.5
packaging==24.2
pandas==2.2.3
parso==0.8.4
platformdirs==4.3.6
prompt_toolkit==3.0.50
psutil==7.0.0
psycopg2==2.9.10
pure_eval==0.2.3
Pygments==2.19.1
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
pytz==2025.1
pywin32==308
pyzmq==26.2.1
requests==2.32.3
six==1.17.0
SQLAlchemy==2.0.38
stack-data==0.6.3
tornado==6.4.2
traitlets==5.14.3
typing_extensions==4.12.2
tzdata==2025.1
urllib3==2.3.0
wcwidth==0.2.13

Licença

Este projeto está sob a licença MIT.


