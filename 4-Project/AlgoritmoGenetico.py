from Populacao import Populacao
from Individuo import Individuo
from random import random


class AlgoritmoGenetico:
    def __init__(self, taxaCrossover, taxaMutacao, geracoes, tamanhoPopulacao, tamanhoCromossomo):
        self.tamaanhoCromossomo = tamanhoCromossomo
        self.taxaCrossover = taxaCrossover
        self.taxaMutacao = taxaMutacao
        self.geracoes = geracoes
        self.tamanhoPopulacao = tamanhoPopulacao
        self.tamanhoCromossomo = tamanhoCromossomo
        self.populacao = Populacao(taxaCrossover, taxaMutacao, tamanhoPopulacao, tamanhoCromossomo)
        
        self.populacao.calculaFitness()
        self.populacao.calculaRangeRoleta()
        
        
    def executaAG(self):
        #populacao.
        print('executando AG')        
        #for novas geracoes
        for i in range(self.geracoes):
            novosIndividuos = self.crossover()
            self.populacao.individuos = novosIndividuos
            self.mutacao()
            self.populacao.evoluir()
            self.populacao.printPopulacao()
        
    def roleta(self):
        numRoleta = random() * 100
        for i in range(self.tamanhoPopulacao):
            if self.populacao.individuos[i].isInRange(numRoleta):
                return i
        return 0
    
    def crossover(self):
        novosIndividuos = []
        
        for i in range( int(self.tamanhoPopulacao / 2)):
            pai = self.populacao.individuos[self.roleta()]
            mae = self.populacao.individuos[self.roleta()]
            
            r = random()
            if(r < self.taxaCrossover):
                corte = round(random() * self.tamanhoCromossomo)
                
                cromF0 = pai.cromossomo[0:corte] + mae.cromossomo[corte::]
                cromF1 = mae.cromossomo[0:corte] + pai.cromossomo[corte::]
                
                filho0 = Individuo(self.tamanhoCromossomo)
                filho1 = Individuo(self.tamanhoCromossomo)
                filho0.cromossomo = cromF0
                filho1.cromossomo = cromF1 
                
                novosIndividuos.append(filho0)
                novosIndividuos.append(filho1)
            else:
                novosIndividuos.append(pai)
                novosIndividuos.append(mae)                
            
        return novosIndividuos
        
        
    def mutacao(self):
        for i in range(len(self.populacao.individuos)):
            self.populacao.individuos[i].mutatBit(self.taxaMutacao)
