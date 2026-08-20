
caso_de_testes = int(input())

for _ in range(caso_de_testes):
    caso_de_testes = input()
    pilha = []
diamantes = 0

for caractere in caso_de_testes:

        if caractere == "<":
                pilha.append(caractere)
                

        elif caractere == ">":
                 if len(pilha) > 0:
                    pilha.pop()
                    diamantes += 1
                    

        print(diamantes)



casos = int(input())

for _ in range(casos):
    caso = input()

    pilha = []
    diamantes = 0

    for caractere in caso:
        if caractere == "<":
            pilha.append(caractere)

        elif caractere == ">":
            if len(pilha) > 0:
                pilha.pop()
                diamantes += 1

    print(diamantes)
             