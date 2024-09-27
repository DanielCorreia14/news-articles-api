News Content Collector and API

Descrição

Este projeto consiste em uma aplicação backend que coleta artigos de um site de notícias, limpa os dados e os armazena no BigQuery. Além disso, uma API é disponibilizada para permitir a busca por artigos usando palavras-chave.

Tecnologias Utilizadas

- Python: Linguagem de programação para implementar a aplicação.
- Flask: Framework para construção da API.
- Scrapy: Framework para web scraping e coleta de dados.
- Readability: Biblioteca para limpeza do conteúdo das páginas web.
- Google BigQuery: Armazenamento e consulta de dados.
- Ngrok: Para expor a API localmente a uma URL pública.

Estrutura do Projeto

news_crawler/
    ├── news_crawler/
    │   ├── __pycache__/
    │   ├── api/
    │   │   ├── app.py
    │   │   └── app.yaml
    │   ├── spiders/
    │   │   ├── __pycache__/
    │   │   ├── __init__.py
    │   │   ├── articles.json
    │   │   ├── bigquery_uploader.py
    │   │   ├── cleaner_articles.json
    │   │   ├── credentials.json
    │   │   ├── data_cleaner.py
    │   │   ├── news.py
    │   │   └── test_connection.py
    │   ├── __init__.py
    │   ├── items.py
    │   ├── middlewares.py
    │   ├── pipelines.py
    │   └── settings.py
    ├── scrapy.cfg
    └── test.py
venv/
README/

Instalação

1. Clone o repositório:

git clone https://github.com/seu_usuario/news_content_collector.git
cd news_content_collector

2. Instale as dependências:

pip install -r requirements.txt

3. Configure as credenciais do Google Cloud:

Crie um arquivo credentials.json com suas credenciais do Google Cloud e coloque-o na pasta api/.
Execução
Executando o Scraper
Para coletar artigos do site de notícias:


4. Para coletar artigos do site de notícias:

python scraper/scraper.py
Executando a API

5. Para iniciar a API em Flask:

python api/app.py
Usando o Ngrok

6. Abra um terminal e execute o ngrok para expor a API:

ngrok http 5000
Copie o link gerado pelo ngrok (ex: https://20e2-179-98-136-19.ngrok-free.app/).

7. Usando a API

Endpoint: GET /articles
Parâmetros:
keyword: Palavra-chave para pesquisa nos títulos dos artigos.

Exemplo de Requisição

GET https://20e2-179-98-136-19.ngrok-free.app/articles?keyword=british

A resposta será um JSON contendo os artigos correspondentes à pesquisa:


[
  {
    "published_date": "Thu, 26 Sep 2024 09:49:45 GMT",
    "title": "‘Thrown like a rag doll’: British tourist narrowly survives hippo attack in Zambia",
    "url": "https://www.theguardian.com/world/2024/sep/26/british-tourist-narrowly-survives-hippo-attack-zambia"
  }
]
