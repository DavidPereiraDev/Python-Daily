class Pilha:
    def  __init__(self):
        self.elements = []
    def push(self,valor):
        self.elements.append(valor)
    def isempty(self):
        return len(self.elements) == 0 
    def pop(self):
        if self.isempty:
            return None
        return self.elements.pop()
    def peek(self):
        if self.isempty:
            return None
        return self.elements[-1]
    def size(self):
        return len(self.elements)
    def show(self):
        return self.elements



