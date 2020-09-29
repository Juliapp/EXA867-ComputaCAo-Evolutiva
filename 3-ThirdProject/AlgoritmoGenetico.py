from Populacao import Populacao
from random import random

class AlgoritmoGenetico:
    def __init__(self, taxaCrossover, taxaMutacao, geracoes, tamanhoPopulacao):
        self.taxaCrossover = taxaCrossover
        self.taxaMutacao = taxaMutacao
        self.geracoes = geracoes
        self.populacao = Populacao(taxaCrossover, taxaMutacao, tamanhoPopulacao)
        
        
    def executaAG(self):
        #populacao.
        print('executando AG')
        self.populacao.calculaFitness()
        self.populacao.calculaRangeRoleta()
        
    def roleta(self):
        numRoleta = random.random() * 100
        for i in range(self.tamanhoPopulacao):
            if self.populacao.individuos[i].isInRange(numRoleta):
                return i
        return 0
    
    def crossover(self):
        print('crossingover')
        
    def mutacao(self):
        print('mutacao')