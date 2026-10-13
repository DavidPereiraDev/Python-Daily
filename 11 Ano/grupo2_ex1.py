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

#prog principal 

pilha_prin = Pilha()

pilha_prin.push(7)
pilha_prin.push(27)
pilha_prin.push(71)
pilha_prin.push(73)
pilha_prin.pop()
pilha_prin.pop()
