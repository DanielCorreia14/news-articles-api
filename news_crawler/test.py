import requests

# URL da página que você deseja analisar
url = 'https://www.theguardian.com/world'

# Faz uma requisição para obter o conteúdo da página
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Imprime o conteúdo HTML da página
    print(response.text)
else:
    print(f'Erro ao acessar a página: {response.status_code}')
