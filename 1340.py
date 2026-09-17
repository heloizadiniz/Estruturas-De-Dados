#EOF limitar memoria, arquivo
#STACK pilha 
#QUEUE fila
#PRIORIRT QUEUE fila de prioridade
#IMPOSSIBLE n pode ser uma pilha, fila e fila de prioridade
# NOT SURE pode ser mais de uma das três estruturas mencionadas a cima

#heapq() modulo de heap, implementa uma fila de prioridade

from collections import deque
#DEQUE estruturar filas 
import heapq

while True:
    try:
        N = int(input())
    except EOFError:
        break

    pilha =[]
    #vetorizar a pilha
    fila = deque()
    prioridade = []

    epilha = True
    efila = True
    eprioridade = True

    for _ in range(N):
    #estrutura de repetição for, para cada elemento em range(N)
    
        operacao, valor = map(int, input().split())
        #map() aplica a função int() a cada elemento do input().split()

        if operacao == 1:
            pilha.append(valor)
            fila.append(valor)
            heapq.heappush(prioridade, -valor)

        else: 
            if not pilha:
                
                epilha = False
            else: 
                remevido = pilha.pop()
            #pop remove o ultimo elemento da pilha
            
                if remevido != valor:
                    epilha = False


            if not fila:
                
                efila = False
            else: 
                remevido = fila.popleft()
            #popleft remove o primeiro elemento da fila
            
        
                if remevido != valor:
                    efila = False

            if not prioridade:
                
                eprioridade = False
            else: 
                remevido = heapq.heappop(prioridade)
            #heappop remove o menor elemento da fila de prioridade
            
                if remevido != valor:
                    eprioridade = False

    possibilidades = sum([
        epilha,
        efila,
        eprioridade
    ])

    if possibilidades == 0:
        print("impossible")

    elif possibilidades > 1: 
        print("not sure")

    elif epilha:
        print("stack")

    elif efila:
        print("queue")

    else:
        print("priority queue")
