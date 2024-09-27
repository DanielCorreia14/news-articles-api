import json

def load_data(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def clean_data(data):
    cleaned_data = []
    for article in data:
        print("Analisando artigo:", article)
        if article.get('title') and article.get('url') and article.get('date'):
            cleaned_data.append(article)
        else:
            print("Artigo ignorado:", article)

    return cleaned_data

def save_cleaned_data(cleaned_data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    data = load_data('articles.json')
    cleaned_data = clean_data(data)
    save_cleaned_data(cleaned_data, 'cleaned_articles.json')

    print("Limpeza de dados concluída! Dados salvos em 'cleaned_articles.json'")
