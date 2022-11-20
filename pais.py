from countryinfo import CountryInfo

country = CountryInfo(input("Digite o nome do pais: "))

print(f"Pais: {country.name()}")
print(f"Capital: {country.capital()}")
print(f"Moedas: {country.currencies()}")
print(f"Idiomas: {country.languages()}")
print(f"Fazem fronteira: {country.borders()}")
print(f"Codigo de area: {country.calling_codes()}")
print(f"Populacao: {country.population()}")
