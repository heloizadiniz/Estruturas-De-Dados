from bisect import bisect_left 
#FROM para chamar uma biblioteca
caso = 1 

while True: 
    N, Q = map(int, input().split())
    if N == 0 and Q == 0:
        break

#MAP para aceitar 2 na mesma linha ou mais variavel no codigo
#WHILE chegar no 0 
    marmores = []

    for _  in range(N):
        marmores.append(int(input()))

#APPEND armazenar numa sequência logica, ordem
    marmores.sort()
#SORT identificar a posição do nome
    print(f"CASE# {caso}:")

    for _ in range(Q):
        numero = int(input())

        posicao = bisect_left(marmores, numero)

        if posicao < N and marmores [posicao] == numero: 
            print(f"{numero} found at {posicao+1}")
        else:
            print(f"{numero} not found")

    caso += 1 