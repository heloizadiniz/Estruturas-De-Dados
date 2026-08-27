# Lê a quantidade de casos de teste
casos = int(input())

# Repete o código para cada caso de teste
for caso in range(casos):

    # Lê dois números inteiros:
    # M = tamanho da tabela
    # C = quantidade de elementos que serão inseridos
    M, C = map(int,input().split())
# Cria uma tabela com M posições.
    # Cada posição começa como uma lista vazia.
    # Exemplo: se M = 5:
    # tabela = [[], [], [], [], []]
    tabela = [[] for _ in range(M)]

    valores = list(map(int, input().split()))

    for valor in valores:
        posicao = valor % M

        tabela[posicao].append(valor)
        #Toda vez q digitar o numero joga pros vetores[]

    for i in range (M):
        print(f"{i} ->", end ="")

        for valor in tabela[i]:
            print(f" {valor} ->", end="")
        print()
    if caso < casos - 1:
        print()    