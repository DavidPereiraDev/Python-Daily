#Crie um menu com as opções: 1) Adicionar cliente à fila, 2) Chamar próximo cliente, 3) Mostrar fila, 4) Sair.
from collections import deque
fila = deque()
while True:
    print("""=====Atendimento Bancário=====
    1-Adicionar cliente a fila
    2-Chamar próximo cliente
    3-Mostrar fila
    4-Sair
=====Atendimento Bancário====
    """)
    op = input("Digite a opção: ") 
    if op == "1":
        c = input("Digite o nome do cliente: ")
        fila.append(c)
        print(fila)
    elif op == "2":
        if len(fila) == 0:
            print("Erro!,a Fila não tem clientes:")
        print(f"Cliente  chamado : {fila.popleft()}")
    elif op == "3":
        if len(fila) == 0:
            print("A Fila não tem clientes")
        else:
            print(f"Estado da fila: {",".join(fila)}")
    elif op == "4":
        break