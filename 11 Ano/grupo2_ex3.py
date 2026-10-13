class Pilha:
    def __init__(self):
        self.elements = []

    def push(self, valor):
        self.elements.append(valor)

    def is_empty(self):
        return len(self.elements) == 0 

    def pop(self):
        if  self.is_empty():
            return None
        return self.elements.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.elements[-1]

    def size(self):
        return len(self.elements)

    def show(self):
        return self.elements
    
#Programa principal

qn = int(input("Quantos números quer inserir: " ))
pilha32 = Pilha()
i = 0
while i != qn : 
    n = int(input("Número : "))
    pilha32.push(n)
    i += 1 
inverso = []
while not  pilha32.is_empty():
    inverso.append(pilha32.pop())
print(inverso)


