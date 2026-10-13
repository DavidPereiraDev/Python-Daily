class Pilha:
    
    def __init__(self):
        self.dados = []

    def push(self, valor):
        self.dados.append(valor)

    def pop(self):
        if not self.is_empty():
            return self.dados.pop()
        raise IndexError("A pilha está vazia")

    def peek(self):
        if not self.is_empty():
            return self.dados[-1]
        raise IndexError("A pilha está vazia")

    def is_empty(self):
        return len(self.dados) == 0

    def clear(self):
        self.dados.clear()


class HistoricoNavegador:
    
    def __init__(self):
        self.pagina_atual = ""
        self.pilha_voltar = Pilha()

    def visitar_site(self, novo_site):
        if self.pagina_atual:
            self.pilha_voltar.push(self.pagina_atual)

        self.pagina_atual = novo_site
        print(f" Acessou: {self.pagina_atual}")

    def botao_voltar(self):
        if not self.pilha_voltar.is_empty():
            self.pagina_atual = self.pilha_voltar.pop()
            print(f"⬅Voltou para: {self.pagina_atual}")
        else:
            print(" Não há páginas anteriores no histórico.")


nav = HistoricoNavegador()

while True:
    comando = input("Escreva um site para visitar, 'voltar' ou 'sair': ")

    if comando.lower() == "sair":
        break
    if comando.lower() == "voltar":
        nav.botao_voltar()
    elif comando:
        nav.visitar_site(comando)
