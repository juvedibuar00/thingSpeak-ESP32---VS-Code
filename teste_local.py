import time
import random
import requests

# ===== CONFIG THINGSPEAK =====
API_KEY = "SUA_WRITE_API_KEY"
URL = "https://api.thingspeak.com/update"

while True:
    # Simulação do sensor
    temperatura = random.randint(20, 35)
    umidade = random.randint(40, 80)

    print("Temp:", temperatura)
    print("Umid:", umidade)

    try:
        response = requests.get(URL, params={
            "api_key": API_KEY,
            "field1": temperatura,
            "field2": umidade
        })

        print("Resposta:", response.text)

    except Exception as e:
        print("Erro:", e)

    time.sleep(15)