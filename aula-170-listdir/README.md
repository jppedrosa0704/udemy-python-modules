# Listagem de Pastas e Imagens com `os` em Python

Este script percorre um diretório específico no sistema e lista todas as pastas encontradas, bem como os arquivos (imagens ou outros) dentro de cada uma delas.  
É útil para organizar coleções de imagens, verificar estrutura de diretórios ou automatizar tarefas de inspeção de arquivos.

---

## 🧠 O que o código faz

1. **Define um caminho base** usando `os.path.join`, garantindo compatibilidade com Windows.
2. **Lista todas as pastas** dentro do diretório informado.
3. Para cada pasta:
   - Verifica se realmente é uma pasta (`os.path.isdir`).
   - Lista todos os arquivos dentro dela.
4. Exibe a estrutura no terminal com indentação.

---

## 📂 Estrutura do Código

```python
import os

caminho = os.path.join('\\Users', 'jp-pe', 'OneDrive', 'Área de Trabalho', 'joaopaulo')

for pasta in os.listdir(caminho):
    caminho_pasta = os.path.join(caminho, pasta)
    print(pasta)
    if not os.path.isdir(caminho_pasta):
        continue
    
    for imagem in os.listdir(caminho_pasta):
        print('\t', imagem)

📝 Explicação das Funções Usadas
os.path.join()  
Constrói caminhos de forma segura e compatível com o sistema operacional.

os.listdir()  
Lista arquivos e pastas dentro de um diretório.

os.path.isdir()  
Verifica se o caminho é uma pasta (evita tentar listar arquivos como se fossem diretórios).
