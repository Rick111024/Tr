import requests
import os


api_key = os.environ.get("API_KEY")


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

data = "2025"
query = input("Qual vai ser a busca? ")
query = query + " " + data

get_noticias(api_key, query)

