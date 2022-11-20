import requests

url = "https://economia.awesomeapi.com.br/all/EUR-BRL"

response = requests.get(url)

if response.status_code == 200:
    dolar_value = float(response.json()["EUR"]["low"])
    print(f"O valor do Euro e R$ {dolar_value:.2f}")
else:
    print("Erro ao buscar valor do Euro")