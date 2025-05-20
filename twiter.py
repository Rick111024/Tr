import os
import requests
from requests.structures import CaseInsensitiveDict

# Carregar os secrets do ambiente
api_key = os.environ.get("TWITTER_API_KEY")
api_secret_key = os.environ.get("TWITTER_API_SECRET_KEY")
bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")

# Verificar se todos os secrets foram carregados corretamente
if not api_key or not api_secret_key or not bearer_token:
    print("❌ Um ou mais secrets não foram encontrados!")
else:
    # Solicitar o nome de usuário ao invés de inserir diretamente
    username = input("Digite o nome de usuário do Twitter: ")  # Exemplo: elonmusk
    
    # URL para buscar o ID do usuário
    user_url = f"https://api.twitter.com/2/users/by/username/{username}"

    # Cabeçalhos de autenticação com o Bearer Token
    headers = CaseInsensitiveDict()
    headers["Authorization"] = f"Bearer {bearer_token}"
    headers["Content-Type"] = "application/json"

    # Realizar a requisição para a API para obter o ID do usuário
    user_response = requests.get(user_url, headers=headers)

    if user_response.status_code == 200:
        user_data = user_response.json()
        user_id = user_data['data']['id']  # Obter o ID do usuário

        # Agora, buscar os tweets do usuário com o ID
        tweets_url = f"https://api.twitter.com/2/users/{user_id}/tweets"

        # Realizar a requisição para buscar os tweets
        response = requests.get(tweets_url, headers=headers)

        if response.status_code == 200:
            tweets = response.json()
            if tweets and 'data' in tweets:
                print(f"🦸 Últimos Tweets de {username}:")
                for tweet in tweets['data']:
                    print(f"- {tweet['text']}")
            else:
                print("Não há tweets disponíveis.")
        else:
            print(f"❌ Erro ao acessar os tweets: {response.status_code}")
    else:
        print(f"❌ Erro ao acessar o usuário {username}: {user_response.status_code}")
