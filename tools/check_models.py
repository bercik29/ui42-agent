import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
url = "https://api.anthropic.com/v1/models"

headers = {
    "X-API-Key": api_key,
    "anthropic-version": "2023-06-01"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    models = response.json().get('data', [])
    print("API kľúč má prístup k týmto modelom:")
    for model in models:
        print(f" - {model['id']}")
else:
    print(f"Chyba {response.status_code}: {response.text}")
    