from random import random

def binaryToInt(binaryList):
    str1 = ""
    str1 = str1.join(binaryList)
    return int(str1, 2)

class Individuo :
    def __init__(self):
        self.cromossomo = []
        self.fitness = 0
        self.fitnessPercent = 0
        self.faixaRoleta = []
        
        self.randomCromossomo()

        
    #preencher o cromossomo de forma aleatória
    def randomCromossomo(self):
        for i in range(8):
            if random() < 0.5:
                self.cromossomo.append("0")
            else:
                self.cromossomo.append("1")
    
    #Função pra mutar o bit
    def mutatBit(self, taxa_mutacao):
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if self.cromossomo[i] == '1':
                    self.cromossomo[i] = '0'
                else:
                    self.cromossomo[i] = '1'     
                    
    
    def isInRange(self, num):
        if num >= self.faixaRoleta[0] and num <= self.faixaRoleta[1]:
            return True
        else:
            return False
    
    def printCromossomo(self):
        print('Cromossomo: ' + str(self.cromossomo) + ' | Fitness: ' + str(self.fitness))
        
    '''
    def crossover(self, outro_individuo):
        corte = round(random()  * len(self.cromossomo))
        
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]
        
        filhos = [Individuo(), Individuo()]
        
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        return filhos
      '''  