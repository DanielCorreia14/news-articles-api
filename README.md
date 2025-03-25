# news-articles-api




## News Crawler and API Project
This project develops a backend application to collect, clean and store news articles in a BigQuery database, in addition to providing an API for searching for keywords in the articles.

## Technologies Used
Python
Scrapy: Collecting news articles.
Readability: Cleaning the article data.
Google Cloud BigQuery: Storing the articles.
Flask: Creating the API.
Ngrok: Exposing the API for external access.

## Features
Article Collection: Uses Scrapy to search for articles from a news website.
Data Cleaning: Filters the content of the articles, removing unnecessary elements.
Storage: Inserts the cleaned data into a table in BigQuery.
Search API: Developed with Flask, it allows searching for articles by keyword.
External Exposure: The API is accessible over the internet via Ngrok.
