import requests
import os

GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

headers = {
    'Authorization': f'token {GITHUB_TOKEN}'
}

def get_user_repos(username):
    response = requests.get(f"{GITHUB_API_URL}/users/{username}/repos", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
