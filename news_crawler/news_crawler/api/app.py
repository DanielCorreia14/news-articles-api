import os
from flask import Flask, request, jsonify
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/mnt/c/Users/danma/Desktop/Projetos/testeLima/news_crawler/news_crawler/api/credentials.json"

app = Flask(__name__)
client = bigquery.Client()

@app.route('/')
def index():
    return "Bem-vindo à API de Artigos!"

@app.route('/articles', methods=['GET'])
def get_articles():
    keyword = request.args.get('keyword', '')

    query = f"""
    SELECT title, url, published_date
    FROM `robust-solution-436815-r5.news_articles_dataset.news_articles_table`
    WHERE LOWER(title) LIKE '%{keyword.lower()}%'
    """

    query_job = client.query(query)
    articles = [dict(row) for row in query_job]

    return jsonify(articles)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
