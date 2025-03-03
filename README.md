# ETL - APHEX TWIN

Um projeto Python para extrair, processar e analisar dados do compositor Aphex Twin. Os dados são salvos em arquivos CSV e Excel para facilitar a análise e o compartilhamento.

---

## Objetivo

O objetivo deste projeto é:
- Extrair dados de artistas, álbuns e músicas do Spotify usando a API oficial.
- Processar e limpar os dados para remover informações desnecessárias.
- Salvar os dados processados em arquivos CSV e Excel.
- Mover os arquivos gerados para um diretório de destino organizado.
- Aprender com a resolução de erros e bugs

---

## Tecnologias Utilizadas

- **Linguagens**: Python
- **Bibliotecas**: Pandas, Requests, Openpyxl, Dotenv
- **APIs**: Spotify Web API
- **Ferramentas**: Git, VS Code

---

## Como Funciona

O projeto funciona em várias etapas:
1. **Autenticação na API do Spotify**:
   - Usa as credenciais do cliente (Client ID e Client Secret) para obter um token de acesso.
2. **Extrair dados do Spotify**:
   - Busca informações sobre artistas, álbuns e músicas.
   - Extrai todas as faixas de um artista específico (no caso, Aphex Twin).
3. **Processar os dados**:
   - Remove colunas desnecessárias e limpa os dados.
   - Adiciona informações adicionais, como URLs externas e URIs.
4. **Salvar os dados**:
   - Salva os dados processados em arquivos CSV e Excel.
5. **Organizar os arquivos**:
   - Move os arquivos gerados para um diretório de destino organizado.

---

## Como Configurar e Executar

### Pré-requisitos

- Python 3.x instalado.
- Conta de desenvolvedor no Spotify para obter as credenciais da API (Client ID e Client Secret).
- Bibliotecas Python listadas no `requirements.txt`.

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/GustavoOliveira-jpg/ETL-Aphex-Twin.git
   cd ETL-Aphex-Twin
2. Crie e ative um ambiente virtual
   dentro da pasta do projeto, abra o terminal e exceute
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
3. Instale as Dependências
O projeto usa bibliotecas como pandas, requests, dotenv, etc. Para instalá-las, execute:
    ```bash
    pip install -r requirements.txt


Referências : https://www.youtube.com/watch?v=WAmEZBEeNmg
