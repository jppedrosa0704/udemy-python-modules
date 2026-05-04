# json.dumo e json.load com arquivos

import json
import os

NOME_ARQUIVO = "aula_177.json"
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(# abs: caminho absoluto
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)

filme = {
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": True,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": None
}

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    filme_json = json.load(arquivo)
    print(filme_json)


