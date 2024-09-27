from google.cloud import bigquery
import json

def upload_to_bigquery(json_file, dataset_id, table_id):
    client = bigquery.Client()

    # verifica se a tabela existe
    table_ref = client.dataset(dataset_id).table(table_id)
    try:
        table = client.get_table(table_ref)
        print(f"Tabela encontrada: {table.table_id}")
    except Exception as e:
        print(f"Erro ao obter a tabela: {e}")
        return

    # carrega o arquivo JSON
    try:
        with open(json_file) as f:
            data = json.load(f)
            print(f"Arquivo JSON lido com sucesso, total de artigos: {len(data)}")
    except Exception as e:
        print(f"Erro ao ler o arquivo JSON: {e}")
        return

    # prepara os dados para inserção
    rows_to_insert = []
    for article in data:
        row = {
            'title': article.get('title', 'Unknown Title'),
            'url': article.get('url', ''),
            'published_date': article.get('date', None)  # Usando 'published_timestamp' ao invés de 'published_date'
        }
        rows_to_insert.append(row)

    # insere os dados no BigQuery
    errors = client.insert_rows_json(table, rows_to_insert)
    if errors:
        print(f"Erros ao inserir dados: {errors}")
    else:
        print("Dados inseridos com sucesso no BigQuery.")

if __name__ == "__main__":
    # chame a função com os parâmetros corretos
    upload_to_bigquery("articles.json", "news_articles_dataset", "news_articles_table")
