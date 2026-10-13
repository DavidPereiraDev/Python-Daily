def soma_pilha():
    ps = pilha
    soma = 0
    while len(ps) != 0 :
        soma += ps.pop()
    print("a soma é :",soma)

pilha = [2,3,4,2]
soma_pilha()
