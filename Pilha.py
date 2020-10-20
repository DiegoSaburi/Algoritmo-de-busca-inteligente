from mapa import Mapa

class Pilha:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.cidades = [None]*self.tamanho
        self.topo = -1
    
    def empilhar(self, item):
        if not self.pilhaCheia():
            self.topo += 1
            self.cidades[self.topo] = item
        else:
            print("Pilha Cheia")
            
    def desempilhar(self):
        if not self.pilhaVazia():
            aux = self.cidades[self.topo]
            self.cidades[self.topo] = None
            self.topo -= 1
            return aux
        else:
            print("Pilha Vazia")
            return None
    
    def getTopo(self):
        return self.cidades[self.topo]
    
    def pilhaVazia(self):
        return (self.topo == -1)
    
    def pilhaCheia(self):
        return (self.topo == self.tamanho -1)
    
mapa = Mapa()
pilha = Pilha(5)
pilha.empilhar(mapa.portoUniao)
pilha.empilhar(mapa.campoLargo)
pilha.empilhar(mapa.canoinhas)

aux = pilha.desempilhar()

