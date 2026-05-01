# Leitura Recursiva de Diretórios e Exibição de Tamanhos de Arquivos em Python

Este projeto demonstra como percorrer diretórios de forma **recursiva** usando `os.walk` e como exibir o tamanho de cada arquivo em um formato legível (KB, MB, GB etc.) através de uma função personalizada baseada em logaritmos.

É ideal para auditoria de arquivos, organização de diretórios, análise de espaço em disco e automação de tarefas de inspeção.

---

## 🧠 Funcionalidades do Script

- Percorre **todas as pastas e subpastas** a partir de um diretório base.
- Lista:
  - Diretórios encontrados
  - Arquivos encontrados
  - Tamanho de cada arquivo em formato humano (ex.: `1.25 MB`)
- Usa `os.stat()` para obter metadados dos arquivos.
- Converte bytes em unidades maiores usando logaritmos (`math.log`).

---

## 📂 Código Completo

```python
import math
import os
from itertools import count


def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""

    if tamanho_em_bytes <= 0:
        return "0B"

    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    potencia = base ** indice_abreviacao_tamanhos
    tamanho_final = tamanho_em_bytes / potencia
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


caminho = os.path.join('\\Users', 'jp-pe', 'OneDrive', 'Área de Trabalho', 'joaopaulo')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'pasta atual ', root)
    
    for dir_ in dirs:
        print('  ', the_counter, 'dir', dir_)

    for file_ in files:
        caminho_completo = os.path.join(root, file_)
        stats = os.stat(caminho_completo)
        tamanho = stats.st_size
        print('  ', the_counter, 'file', file_, formata_tamanho(tamanho))

📝 Explicação das Principais Partes
🔹 formata_tamanho()
Converte bytes em unidades maiores usando logaritmos:

math.log(tamanho_em_bytes, base) determina qual unidade usar.

Divide o tamanho pela potência correspondente.

Retorna valores como:

512 B

1.23 KB

15.87 MB

2.01 GB

🔹 os.walk()
Percorre diretórios recursivamente, retornando:

root → diretório atual

dirs → subpastas

files → arquivos dentro de root

🔹 os.stat()
Retorna metadados do arquivo, incluindo:

st_size → tamanho em bytes
