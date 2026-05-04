📘 README — Uso de json.dump e json.load com arquivos em Python
Este exemplo demonstra como salvar e carregar dados em formato JSON utilizando as funções json.dump() e json.load() em Python, garantindo que o arquivo seja sempre encontrado através de um caminho absoluto.

📂 Objetivo do código
Criar um dicionário Python representando um filme.

Salvar esse dicionário em um arquivo JSON.

Ler o arquivo JSON de volta para o Python.

Exibir o conteúdo carregado.

🛠️ Tecnologias utilizadas
Python 3

Módulo padrão json

Módulo padrão os

📁 Estrutura do arquivo
O código define:

python
NOME_ARQUIVO = "aula_177.json"
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)
Isso garante que o arquivo JSON será salvo na mesma pasta do script, independentemente de onde o programa for executado.

💾 Salvando dados com json.dump
python
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)
json.dump() escreve o dicionário no arquivo.

ensure_ascii=False mantém acentos e caracteres especiais.

indent=2 deixa o JSON organizado e legível.

📥 Carregando dados com json.load
python
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    filme_json = json.load(arquivo)
    print(filme_json)
json.load() lê o arquivo e converte o conteúdo JSON de volta para um dicionário Python.

📌 Resultado esperado
Ao executar o script, o terminal exibirá:

python
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
✔️ Conclusão
Este exemplo mostra o fluxo completo de:

Criar dados →

Salvar em JSON →

Ler JSON →

Usar novamente no Python

É a base para qualquer sistema que precise persistir dados simples sem banco de dados.
