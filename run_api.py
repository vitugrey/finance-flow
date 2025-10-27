import requests
import os

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

def send_transaction(transaction: dict) -> dict:
    url = f"{API_URL}/transactions/"
    response = requests.post(url, json=transaction)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao enviar transação: {response.text}")