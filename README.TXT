

News Crawler and API Project
Este projeto desenvolve uma aplicação backend para coletar, limpar e armazenar artigos de notícias em um banco de dados BigQuery, além de disponibilizar uma API para busca por palavras-chave nos artigos.

Tecnologias Utilizadas
Python
Scrapy: Coleta de artigos de notícias.
Readability: Limpeza dos dados dos artigos.
Google Cloud BigQuery: Armazenamento dos artigos.
Flask: Criação da API.
Ngrok: Exposição da API para acesso externo.

Funcionalidades
Coleta de Artigos: Usa Scrapy para buscar artigos de um site de notícias.
Limpeza de Dados: Filtra o conteúdo dos artigos, removendo elementos desnecessários.
Armazenamento: Insere os dados limpos em uma tabela no BigQuery.
API de Busca: Desenvolvida com Flask, permite buscar artigos por palavra-chave.
Exposição Externa: A API é acessível pela internet via Ngrok.