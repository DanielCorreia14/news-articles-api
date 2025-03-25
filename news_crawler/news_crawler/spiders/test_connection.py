from google.cloud import bigquery

def test_bigquery():
    client = bigquery.Client()
    datasets = list(client.list_datasets())  # lista todos os datasets no projeto
    if datasets:
        print("Datasets disponíveis no projeto:")
        for dataset in datasets:
            print(dataset.dataset_id)
    else:
        print("Nenhum dataset encontrado no projeto.")

if __name__ == "__main__":
    test_bigquery()
