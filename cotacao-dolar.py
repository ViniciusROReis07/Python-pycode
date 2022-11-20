import requests

url = "https://economia.awesomeapi.com.br/all/USD-BRL"

response = requests.get(url)

if response.status_code == 200:
    dolar_value = float(response.json()["USD"]["low"])
    print(f"O valor do Dolar e R$ {dolar_value:.2f}")
else:
    print("Erro ao buscar valor do Dolar")