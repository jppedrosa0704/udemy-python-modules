📘 README — Manipulação de Arquivos e Pastas com pathlib e shutil em Python
Este script demonstra como trabalhar com caminhos, arquivos e pastas utilizando o módulo moderno pathlib e a função rmtree do módulo shutil. Ele cria diretórios, arquivos, escreve conteúdo, verifica existência e remove itens quando necessário.

🧩 Tecnologias utilizadas
Python 3

pathlib.Path — manipulação moderna de caminhos

shutil.rmtree — remoção recursiva de diretórios

📂 Principais conceitos demonstrados
✔️ 1. Obtendo caminhos com Path(__file__)
python
caminho_arquivo = Path(__file__)
print(caminho_arquivo.parent.parent)
Path(__file__) → caminho completo do arquivo atual.

.parent → pasta onde o arquivo está.

.parent.parent → pasta acima.

✔️ 2. Criando caminhos com o operador /
python
ideias = caminho_arquivo.parent / 'ideias'
O operador / concatena caminhos de forma elegante e segura.

✔️ 3. Criando pastas com mkdir()
python
caminho_pasta = Path.home() / 'Desktop' / 'Pyton é legal'
caminho_pasta.mkdir(exist_ok=True)
Path.home() → pasta do usuário.

exist_ok=True evita erro se a pasta já existir.

Também é criada uma subpasta:

python
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)
✔️ 4. Criando e escrevendo arquivos
python
outro_arquivo = subpasta / 'jp é legal.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey')
touch() cria o arquivo.

write_text() escreve conteúdo.

✔️ 5. Criando vários arquivos em loop
python
files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'
Para cada arquivo:

Se existir → apaga com .unlink()

Se não existir → cria com .touch()

Depois escreve conteúdo com .open('a+')

python
with file.open('a+', encoding='utf-8') as text_file:
    text_file.write('olá mundo\n')
    text_file.write(f'file_{i}.txt')
✔️ 6. Removendo pastas inteiras (opcional)
python
# rmtree(caminho_pasta)
rmtree() apaga a pasta e tudo dentro dela.

📌 Resumo do que o script faz
Identifica o caminho do arquivo atual.

Cria pastas no Desktop:

Pyton é legal

subpasta

files

Cria arquivos dentro dessas pastas.

Escreve conteúdo nos arquivos.

Cria 10 arquivos numerados (file_0.txt até file_9.txt).

Demonstra como apagar arquivos e pastas.

✔️ Conclusão
Este script é um exemplo completo e prático de como usar pathlib para:

Criar caminhos

Criar pastas

Criar arquivos

Escrever conteúdo

Verificar existência

Apagar arquivos

Remover diretórios inteiros

É uma base excelente para qualquer automação de arquivos no Python moderno.
