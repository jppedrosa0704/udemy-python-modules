🎯 O que o teu código faz agora
Define um TypedDict chamado Movie com todos os campos esperados.

Cria uma string JSON com os dados do filme.

Converte essa string para um dicionário Python usando json.loads.

Tipas o resultado como Movie, o que ativa autocomplete no VS Code.

Imprime o dicionário formatado com json.dumps.

O resultado final é um JSON bonito, com acentos preservados:

json
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": [
    "Frodo",
    "Sam",
    "Gandalf",
    "Legolas",
    "Boromir"
  ],
  "budget": null
}
