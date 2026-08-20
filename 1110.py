from collections import deque
#DEQUE estruturar filas 

while True: 
    N = int(input())
#N número inteiro
    if N == 0:
        break
# N for igual a zero o programa fecha

    fila = deque(range(1, N + 1))
# RANGE (Inicio(contandor), Condição , Inerrente(decremente) )
    descartadas = []

    while len(fila) > 1:
        descartadas.append(str(fila.popleft()))

        fila.append(fila.popleft())

#POPLeft numero q descarta da direita 
#STR = string
#LEN armazena a fila

    print("Discarded cards:", ", ".join(descartadas))
    print("Remaining card:", fila[0])

#JOIN juntar 
#Discarded cards = Descarte de cartas
#Remaining = Cartas remanecentes