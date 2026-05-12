# 🧰 Argumentos de Linha de Comando com `argparse.ArgumentParser`

Este projeto demonstra como criar e processar argumentos de linha de comando usando o módulo **argparse**, que é a forma mais poderosa e profissional de lidar com parâmetros em scripts Python.

O script aceita dois tipos de argumentos:

- `-b` / `--basic` → recebe valores (pode ser usado várias vezes)
- `-v` / `--verbose` → ativa modo verboso (booleano)

---

## 📌 Como o Script Funciona

O código cria um parser:

```python
parser = ArgumentParser()
Argumento --basic
python
parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá mundo" na tela',
    metavar='STRING',
    required=False,
    action='append'
)
-b ou --basic

Aceita strings

Pode ser usado mais de uma vez (action='append')

Não é obrigatório

Argumento --verbose
python
parser.add_argument(
    '-v', '--verbose',
    help='Mostra logs',
    action='store_true'
)
-v ou --verbose

Não recebe valor

Se presente → True

Se ausente → False

▶️ Como Executar o Script
Passando um valor para --basic:
bash
python script.py -b teste
Passando vários valores:
bash
python script.py -b um -b dois -b tres
Ativando o modo verbose:
bash
python script.py -v
Usando tudo junto:
bash
python script.py -b ola -b mundo -v
📤 Saída Esperada
Quando --basic não é passado:
Código
Você não passou o valor de b.
None
False
Quando --basic é passado:
Código
O valor de basic: ['ola', 'mundo']
True
🧠 Lógica do Script
python
if args.basic is None:
    print('Você não passou o valor de b.')
    print(args.basic)
else:
    print('O valor de basic:', args.basic)

print(args.verbose)
Se --basic não for usado → imprime aviso

Se for usado → mostra a lista de valores

Sempre imprime o estado de --verbose

🎯 Objetivo do Exemplo
Este script serve como base para:

Criar ferramentas de linha de comando profissionais

Processar múltiplos argumentos

Ativar modos opcionais (como verbose)

Substituir o uso básico de sys.argv

📝 Requisitos
Python 3.x

Execução via terminal (CMD, PowerShell ou VS Code Terminal)

👨‍💻 Autor
Exemplo criado para fins de estudo e prática com o módulo argparse em Python.
