# 🖥️ Uso de Argumentos no Terminal com `sys.argv` em Python

Este projeto demonstra como ler e manipular **argumentos passados pela linha de comando** utilizando o módulo `sys` da biblioteca padrão do Python.  
O objetivo é mostrar como um script pode reagir de forma dinâmica dependendo dos argumentos recebidos.

---

## 📌 Como o Script Funciona

O código utiliza:

```python
import sys
argumentos = sys.argv
qtd_argumentos = len(argumentos)
sys.argv é uma lista contendo:

argv[0] → nome do arquivo Python

argv[1:] → argumentos passados pelo usuário

O script:

Conta quantos argumentos foram recebidos

Exibe todos os argumentos (exceto o nome do arquivo)

Tenta acessar argumentos individuais

Trata erros caso faltem argumentos

🧠 Lógica do Script
python
if qtd_argumentos <= 1:
    print('você não passou argumentos')
else:
    try:
        print(f"você passou os argumento {argumentos[1:]}")
        print(f"faça alguma coisa {argumentos[1]}")
        print(f"falta outra coisa com {argumentos[2]}")
    except IndexError:
        print('faltam argumentos.')
✔ O que ele faz:
Se nenhum argumento for passado → avisa o usuário

Se argumentos forem passados → imprime:

A lista completa de argumentos

O primeiro argumento individual

O segundo argumento individual

Se faltar algum argumento → captura o erro com IndexError

▶️ Como Executar o Script
Abra o terminal na pasta onde o arquivo está e execute:

bash
python aula_187_sys_argv.py teste1 teste2 teste3
Resultado esperado:
Código
