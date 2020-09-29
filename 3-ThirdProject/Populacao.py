from Individuo import Individuo

class Populacao:
    def __init__(self, taxaCrossover, taxaMutacao, tamanhoPopulacao, tamanhoCromossomo):
        self.individuos = []
        self.geracaoAtual = 0
        #inicializando a poopulacao
        for i in range(tamanhoPopulacao):
            self.individuos.append(Individuo(tamanhoCromossomo))
        
    def calculaFitness(self):
        totalFitness = 0;
        
        for i in range(len(self.individuos)):
            x = self.individuos[i].valor
            y = round((10*(x**2)) + (2*x) + 30)
            self.individuos[i].fitness = y
            totalFitness += y
        
        for i in range(len(self.individuos)):
            self.individuos[i].fitnessPercent = (self.individuos[i].fitness/totalFitness) * 100
            
        self.individuos = sorted(self.individuos, key= Individuo.getFitnessPercent, reverse = True)
        
    def calculaRangeRoleta(self):
        roleta = 0
        for i in range(len(self.individuos)):
            esquerda = roleta
            direita = roleta + self.individuos[i].fitnessPercent
            self.individuos[i].faixaRoleta = [esquerda, direita] 
            roleta += self.individuos[i].fitnessPercent
        
    
    def getMediaPopulacao(self):
        soma = 0
        for i in range(len(self.individuos)):
            soma += self.individuos[i].fitness
        
        return soma / len(self.individuos)
    
    def evoluir(self):
        self.geracaoAtual += 1
        self.calculaFitness()
        self.calculaRangeRoleta()
        
    def printPopulacao(self):
        for i in range(len(self.individuos)):
            print('Individuo ' + str(i) + ' da geração ' + str(self.geracaoAtual))
            self.individuos[i].printCromossomo()
            print('')