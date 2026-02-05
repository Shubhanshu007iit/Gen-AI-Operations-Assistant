import requests

def search_github(query):
    url = f"https://api.github.com/search/repositories?q={query}&sort=stars"
    response = requests.get(url)
    data = response.json()
    return data["items"][:3]
