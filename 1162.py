#Aqui o programa pergunta quantos casos de teste serão executados.
casos = int(input())

#RANGE faz a leitura de quantos casos são 
for _ in range(casos):

    #Aqui você recebe a quantidade de vagões.
    n = int(input())

    vagoes = list(map(int, input() .split()))
#.SPLIT divide uma string em uma lista de partes menores
#input() Lê uma linha
#O map(int, ) transforma cada texto em número
#E list() transforma o resultado em uma lista.

    trocas = 0 
    #Essa variável vai guardar quantas vezes dois vagões precisaram trocar de posição.

    for i in range( 1, n ):
    #Aqui começa em 1, porque o programa vai comparar o vagão atual com o anterior.   

        J = i
        #J vai representar a posição do vagão que estamos tentando colocar no lugar correto.

        while J > 0 and vagoes [J] < vagoes [J - 1]:
        #Enquanto J não estiver no começo da lista e o vagão atual for menor que 
        # o vagão anterior, faça uma troca.

            vagoes[J], vagoes [J - 1] = vagoes [J - 1], vagoes[J]

            trocas += 1 

            J -= 1
    print(f"Optimal train swapping takes{trocas} swaps.")
         



