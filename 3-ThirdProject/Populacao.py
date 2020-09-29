from Individuo import Individuo

class Populacao:
    def __init__(self, taxaCrossover, taxaMutacao, tamanhoPopulacao):
        self.individuos = []
        #inicializando a poopulacao
        for i in range(tamanhoPopulacao):
            self.individuos.append(Individuo())
            
    def getPopulacao(self):
        return self.individuos
        
    def setPopulacao(self, individuos):
        self.individuos = individuos
        
    def calcularFitness(self):
        print('calculando fitness')
        
    def calcularFitnessPercent(self):
        print('calculando fitness percent')
    
    def getMediaPopulacao(self):
        soma = 0
        for i in range(len(self.individuos)):
            soma += self.individuos[i].fitness
        
        return soma / len(self.individuos)
        
    def printPopulacao(self):
        for i in range(len(self.individuos)):
            print('Individuo ' + str(i))
            self.individuos[i].printCromossomo()
            print('')