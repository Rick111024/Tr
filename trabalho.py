import requests

def get_noticias(api_key, query):
   url = f"https://newsapi.org/v2/everything?q={query}&pageSize=5&sortBy=publishedAt&apiKey={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        news_data = response.json()
        for article in news_data['articles']:
            print(f"Título: {article['title']}")
            print(f"Descrição: {article['description']}")
            print(f"URL: {article['url']}")
            print("-----------------------------")
    else:
        print("Erro ao buscar notícias")


api_key = '4b9e57dc47ac4e788f439652dffda5d6'
data = "2025"
query = input("Qual vai ser a busca? ")


query = query + " " + data


get_noticias(api_key, query)
