🧱 Estrutura do código
1. Importações
python
import json
import os
from pprint import pprint
from typing import TypedDict
json → para converter JSON ↔ Python

os → usado aqui apenas para limpar o terminal

pprint → impressão formatada (não usada no final)

TypedDict → cria um “modelo” de dicionário tipado

2. Definição do modelo Movie
python
class Movie(TypedDict):
    title : str
    original_title : str
    is_movie : bool
    imdb_rating : float
    year : int
    characters : list[str]
    budget : None | float
Isto define a estrutura esperada do JSON.
Serve para:

autocomplete no VS Code

evitar erros de chave

documentação clara do formato

3. String JSON
python
sstring_json = '''{
"title": "O Senhor dos Anéis: A Sociedade do Anel",
"original_title": "The Lord of the Rings: The Fellowship of the Ring",
"is_movie": true,
"imdb_rating": 8.8,
"year": 2001,
"characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
"budget": null
}
'''

É um JSON real, contendo:

strings

booleanos

números

listas

valor null

4. Carregando o JSON
python
filme: Movie = json.loads(string_json)
Aqui:

json.loads converte a string JSON para um dicionário Python

filme: Movie indica ao editor que esse dicionário segue o modelo Movie

5. Imprimindo o JSON formatado
python
print(json.dumps(filme, ensure_ascii=False, indent=2))
ensure_ascii=False mantém acentos

indent=2 deixa o JSON bonito e legível

📌 Resultado final
O programa imprime o JSON formatado no terminal.
