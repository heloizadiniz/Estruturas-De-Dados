n = int(input())
#n = numeros de casos

for _ in range(n):

    palavras = input().split()
#input vale por letra e numero
#split separação de string

    palavras.sort(key=len, reverse=True)
#sort metodo de ordenação (so maior para o mener, crescente)
#Len retorna o numero de itens e tamanho
#reverse=True reverter o sort

    print(" ".join(palavras))
#print(" ".join(entrada)) organiza por espaço


