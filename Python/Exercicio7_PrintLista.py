if __name__ == '__main__':
    n = int(input())

    # Cria um range de 1 até n+1
    # O * desempacota os números como argumentos individuais
    # sep='' remove os espaços padrão entre os argumentos
    print(*range(1, n + 1), sep='')