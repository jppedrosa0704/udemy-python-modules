# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
#caminho = r'C:\\Users\\jp-pe\\OneDrive\\Área de Trabalho\\joaopaulo'
import os

caminho = os.path.join('\\Users', 'jp-pe', 'OneDrive', 'Área de Trabalho', 'joaopaulo' )

for pasta in os.listdir(caminho):
    caminho_pasta = os.path.join(caminho, pasta)
    print(pasta)
    if not os.path.isdir(caminho_pasta):
        continue
    
    for imagem in os.listdir(caminho_pasta):
        print('\t',imagem)
# caminho = os.path.join('/Users', 'luizotavio', 'Desktop', 'EXEMPLO')

# for pasta in os.listdir(caminho):
#     caminho_completo_pasta = os.path.join(caminho, pasta)
#     print(pasta)

#     if not os.path.isdir(caminho_completo_pasta):
#         continue

#     for imagem in os.listdir(caminho_completo_pasta):
#         print('  ', imagem)
