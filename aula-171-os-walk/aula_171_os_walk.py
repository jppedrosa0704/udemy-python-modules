# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

caminho = os.path.join('\\Users', 'jp-pe', 'OneDrive', 'Área de Trabalho', 'joaopaulo' )
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'pasta atual ', root)
    
    for dir_ in dirs:
        print('  ',the_counter, 'dir', dir_)

    for file_ in files:
        caminho_completo = os.path.join(root, file_)
        print('  ', the_counter, 'file', caminho_completo)

        #os.unlink(caminho_completo ) exclui aqruivos OBS: não executar
        #'vai apagar tudo na pasta

