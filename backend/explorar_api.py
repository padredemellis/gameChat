import os

import httpx
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("CLAVE_FOOTBALL")

url = "https://api.football-data.org/v4/competitions"
headers = {
    "X-Auth-Token": api_key
}
response = httpx.get(url, headers=headers)
print(f"Código de estado: {response.status_code}")
print("Respuesta JSON:")
print(response.json())