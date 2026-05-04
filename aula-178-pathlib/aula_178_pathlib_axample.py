from pathlib import Path
from shutil import rmtree

caminho_arquivo = Path()
# print(caminho.absolute())

caminho_arquivo = Path(__file__)
# print(caminho_arquivo)

print(caminho_arquivo.parent.parent)

ideias = caminho_arquivo.parent / 'ideias' #cria um novo caminho (pasta)
# print(ideias / 'arquivo.txt')

# print(Path.home() / 'Desktop' / 'arquivo.tx')

# arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
# arquivo.touch() #cria um arquivo.txt na desktop
# print(arquivo)
# #arquivo.unlink() #apaga o arquivo

# arquivo.write_text("Olá, mundo!", encoding='utf-8') #escrever no arquivo
# print(arquivo.read_text()) #ler os arquivo no terminal do vscode

#escrever várias linhas

# with arquivo.open('a+',encoding='utf-8') as file:
#     file.write('uma linha\n')
#     file.write('outra linha\n')

# print(arquivo.read_text())

caminho_pasta = Path.home() / 'Desktop' / 'Pyton é legal'
caminho_pasta.mkdir(exist_ok=True)
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / 'jp é legal.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey')

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'
    if file.exists():
        file.unlink()
    else:
        file.touch()

    with file.open('a+', encoding='utf-8') as text_file:
        text_file.write('olá mundo\n')
        text_file.write(f'file_{i}.txt')


# rmtree(caminho_pasta) apaga a pasta e todo o conteudo



