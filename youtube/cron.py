import time
import random
import requests

def call_api():
    # Substitua pela chamada real à sua API
    url = "http://localhost:5000/create_playlist"
    data = {
        "playlist_title": "Músicas Aleatórias",
        "playlist_description": "Playlist criada aleatoriamente a cada 24 horas.",
        "keywords": ["aleatório", "música", "diversão"],
        "max_results": 5
    }
    response = requests.post(url, json=data)
    print(response.json())

def run_cron():
    while True:
        # Esperar 24 horas
        time.sleep(24 * 60 * 60)

        # Gerar um intervalo de tempo aleatório entre 0 e 60 minutos
        random_minutes = random.randint(0, 60)
        random_seconds = random_minutes * 60

        # Esperar o tempo aleatório adicional
        print(f"Aguardando {random_minutes} minutos antes da próxima execução...")
        time.sleep(random_seconds)

        # Chamar a API
        print("Executando a API...")
        call_api()

if __name__ == '__main__':
    run_cron()
