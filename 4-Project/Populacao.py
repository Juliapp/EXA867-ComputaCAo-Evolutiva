from Individuo import Individuo
import math
import matplotlib.pyplot as plt

functionXSize = 0
media = []

class Populacao:
    def __init__(self, taxaCrossover, taxaMutacao, tamanhoPopulacao, tamanhoCromossomo):
        functionXSize = 2**tamanhoCromossomo
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
        
        media.append(self.getMediaPopulacao())
        
        plotGraficos(len(self.individuos), self.geracaoAtual, self.individuos, media)
        
    def printPopulacao(self):
        for i in range(len(self.individuos)):
            print('Individuo ' + str(i) + ' da geração ' + str(self.geracaoAtual))
            self.individuos[i].printCromossomo()
            print('')
            
            
def funcao1(x):
    return 100 + math.fabs(x * math.sin(math.sqrt(math.fabs(x))))

def plotFuncao1(functionXSize):
    y = []
    x = []
    for i in range(400):
        x.append(i)
        y.append(funcao1(i))
    plt.plot(x,y, color='r', linewidth=2.0)
    
def plotPop(TAM_POPULACAO, pop):
    x_pop = []
    y_pop = []   
    for i in range(TAM_POPULACAO):
        x_pop.append(pop[i].valor)
        y_pop.append(funcao1(pop[i].valor))
    plt.stem(x_pop, y_pop, use_line_collection=True)
    
def plotGraficos(TAM_POPULACAO, geracao, pop,media):
    plt.title(geracao, fontdict=None, loc='center', pad=None)
    plotFuncao1(functionXSize)
    plotPop(TAM_POPULACAO, pop)
    #plt.plot(media, color='b', linewidth=1.0)
    plt.show()
    
def plotMedia(media):
    plt.plot(media, color='b', linewidth=1.0)
    plt.show()