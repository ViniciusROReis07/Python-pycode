from googlesearch import search

query = "Selecao brasileira futebol"

result = list(
    search(
        query,
        lang="pt-br",
        num_results=5
    )
)

print(result)