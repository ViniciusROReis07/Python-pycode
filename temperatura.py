from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/558/itaoevi-sp").content

soup = BeautifulSoup(html, "html.parser")

tempMin = soup.find(id="min-temp-1")
tempMax = soup.find(id="max-temp-1")

print("Temp. Minina: " + tempMin.string)
print("Temp Maxima: " + tempMax.string)