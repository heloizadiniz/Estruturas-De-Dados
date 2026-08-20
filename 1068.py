while True: 
    try:
        expressao = input()
#WHILE não tem limite FOR tem!
        pilha = []
        correta = True

        for caractere in expressao:

            if caractere == "(":
                pilha.append(caractere)
#APPEND armazenar numa sequência logica, ordem

#ELIF continuidade do if
            elif caractere == ")":

                if len(pilha) == 0:
                    correta = False
                    break
#POP método para sustentar a pilha
                pilha.pop()

        if correta and len(pilha) == 0:
            print("Correct")
        else:
            print("incorrect")
#EXCEPT exeção de memoria
    except EOFError:
        break             