from Pilha import Pilha
from cidade import Cidade
from mapa import Mapa

class Profundidade:
    def __init__(self, inicio : Cidade , objetivo : Cidade):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.fronteira = Pilha(20)
        self.fronteira.empilhar(inicio)
        self.achou = False
        
    def buscar(self ):
        topo = self.fronteira.getTopo()
        print(f"topo: {topo.nome}")
        if topo == self.objetivo:
            self.achou = True
        else:
            for adjacente in topo.adjacentes:
                if self.achou == False:                
                    print(f"Verificando se ja foi visitado: {adjacente.cidade.nome}")                
                    if adjacente.cidade.visitado == False:
                        adjacente.cidade.visitado = True
                        self.fronteira.empilhar(adjacente.cidade)
                        self.buscar()
        print(f"Desempilhou: {self.fronteira.desempilhar().nome}")
        
mapa = Mapa()
profundidade = Profundidade(mapa.portoUniao, mapa.curitiba)
profundidade.buscar()
