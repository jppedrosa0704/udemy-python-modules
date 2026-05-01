# Navegando Diretórios Recursivamente com `os.walk` em Python

Este projeto demonstra como percorrer diretórios de forma **recursiva** utilizando a função `os.walk`, exibindo pastas, subpastas e arquivos encontrados.  
É útil para inspeção de estruturas de diretórios, organização de arquivos, automação de tarefas e auditoria de sistemas de arquivos.

---

## 🧠 O que o script faz

1. Define um **caminho base** usando `os.path.join`.
2. Usa `os.walk` para navegar por todas as pastas e subpastas.
3. Para cada diretório encontrado:
   - Exibe o número sequencial da iteração.
   - Lista subdiretórios.
   - Lista arquivos com seus caminhos completos.
4. Mantém um contador global usando `itertools.count()`.

---

## 📂 Código Completo

```python
import os
from itertools import count

caminho = os.path.join('\\Users', 'jp-pe', 'OneDrive', 'Área de Trabalho', 'joaopaulo')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'pasta atual ', root)
    
    for dir_ in dirs:
        print('  ', the_counter, 'dir', dir_)

    for file_ in files:
        caminho_completo = os.path.join(root, file_)
        print('  ', the_counter, 'file', caminho_completo)

        # os.unlink(caminho_completo)  # EXCLUI ARQUIVOS — NÃO EXECUTAR SEM CERTEZA
