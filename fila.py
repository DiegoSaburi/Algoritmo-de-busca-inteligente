from cidade import Cidade

class Fila:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.cidades = [None]*self.tamanho
        self.inicio = 0
        self.fim = -1
        self.numeroElementos = 0
        
    def enfileirar(self, cidade : Cidade):
        if not self.filaCheia(): 
            if self.fim == self.tamanho - 1:
                self.fim = -1
            self.fim += 1
            self.cidades[self.fim] = cidade
            self.numeroElementos += 1
        else:
            print("Fila cheia")
    
    def desenfileirar (self):
        if not self.filaVazia():
            aux = self.cidades[self.inicio]
            self.cidades = None
            self.inicio += 1
            if self.inicio == self.tamanho:
                self.inicio = 0
            self.numeroElementos -= 1
            return aux
        else:
            print("Fila vazia")
            return None
    
    def getPrimeiro(self):
        return self.cidades[self.inicio]
    
    def filaVazia(self):
        return self.numeroElementos == 0
    
    def filaCheia(self):
        return self.numeroElementos == self.tamanho
