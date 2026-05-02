# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename

import os
import shutil

HOME = os.path.expanduser('~') #home do usuário
DESKTOP = os.path.join(HOME, 'Desktop')#C:\Users\jp-pe\Desktop
PASTA_ORIGINAL = os.path.join(DESKTOP, 'joaopaulo') #C:\Users\jp-pe\Desktop\joaopaulo
NOVA_PASTA =  os.path.join(DESKTOP, 'NOVA_PASTA') #C:\Users\jp-pe\Desktop\NOVA_PASTA

#shutil.rmtree(NOVA_PASTA) deleta uma pasta
#os.unlink(nomedapasta) #apaga arquivos
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)

# os.rename(NOVA_PASTA, 'copia do joaopaulo')
#  OU
shutil.move(NOVA_PASTA, NOVA_PASTA + 'copia do joao paulo')

