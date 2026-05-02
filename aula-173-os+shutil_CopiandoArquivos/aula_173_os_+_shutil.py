# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil
# %USERPROFILE% ver a home do usuario
# echo %USERPROFILE%\Desktop  caminho da area de trabalho (desktop)
# dir "%USERPROFILE%\OneDrive\Área de Trabalho"  posso ver o conteudo da area de trabalho
HOME = os.path.expanduser('~') #Home do usuário C:\Users\jp-pe
DESKTOP = os.path.join(HOME, 'Desktop') # C:\Users\jp-pe\Desktop
print(DESKTOP)

PASTA_ORIGINAL = os.path.join(DESKTOP, 'joaopaulo') #C:\Users\jp-pe\Área de Trabalho\joaopaulo
print(PASTA_ORIGINAL)
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')
os.makedirs(NOVA_PASTA, exist_ok=True) #cria nova pasta
# print(NOVA_PASTA)
# dir "C:\Users\jp-pe\Área de Trabalho\joaopaulo" mostra as pastas existentes


for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )
        os.makedirs(caminho_novo_diretorio, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
        )
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)

