import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

print(qtd_argumentos)

if qtd_argumentos <= 1:
    print('você não passou argumentos')

else:
    try:
        print(f"você passou os argumento {argumentos[1:]}")
        print(f"faça alguma coisa {argumentos[1]}")
        print(f"falta outra coisa com {argumentos[2]}")

    except IndexError:
        print('faltam argumentos.')
