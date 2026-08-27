# Lê a quantidade de casos de teste
n = int(input())

# Percorre cada caso de teste
for caso in range(n):
    # Lê o texto que será analisado

    texto = input()
    # Cria um dicionário vazio para guardar a frequência de cada caractere.
  
    frequencia = {}
    # Percorre cada caractere do texto ex ord('A') = 65

    for caractere in texto:
        codigo = ord(caractere)
        # ord() transforma o caractere no seu código numérico.

    if codigo not in frequencia:
        frequencia[codigo] = 0 
        #Se for a primeira vez que encontramos esse caractere, começamos sua frequência em 0

    frequencia[codigo] += 1
    # Aumenta em 1 a quantidade de vezes que esse caractere apareceu Exemplo:
    # frequencia = {65: 3, 66: 1, 67: 2}

    caractere = list(frequencia.keys())
    # Ordena os códigos de acordo com dois critérios:
    # 1º - frequência em ordem crescente
    # 2º - código em ordem decrescente

    caractere.sort(
        key=lambda codigo: (frequencia[codigo], -codigo)
        # Mostra o código do caractere e sua frequência

    )

    for codigo in caractere: 
        print(codigo, frequencia[codigo])
    # Se ainda não estamos no último caso, imprime uma linha vazia para separar os resultados dos casos de teste.
    if caso < n - 1:
        print()