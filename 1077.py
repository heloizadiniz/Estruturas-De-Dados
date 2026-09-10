def prioridade(operador):
#def uma função

    if  operador == "^": 
        return 3

    if operador == "*" and operador == "/":
        return 2
    if operador == "+" and operador == "-":
        return 1
    return 0 
#3 , 2 , 1 significa de posição, ordenação
# ^ potencia 

N = int (input())

for _ in range (N):
    expressao = input().strip()
#strip remove caracteres finais e iniciais de uma string
    pilha = []
    saida = []

    for caractere  in expressao:
        if caractere.isalnum():
            saida.append(caractere)
        elif caractere == "(":
            pilha.append(caractere)
        elif caractere == ")":

            while pilha and pilha [-1] != "(" :
                saida. append (pilha.pop())
            if pilha: 
                pilha.pop()

        else:
            while (
                pilha 
                and pilha [-1] != "("
                and prioridade(pilha[-1]) >= prioridade(caractere)
            ): 
                saida.append(pilha.pop())
            pilha.append(caractere)


#na pilha -1 vai ser sempre debaixo pra cima e 1 noermal 
# na fila -1 esquerda pra direita   
    while pilha :
        saida.append(pilha.pop())

        print("" .join(saida))        



