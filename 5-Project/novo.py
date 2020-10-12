import numpy as np
from random import randint

class Jogo:
    ####################### CONSTRUTOR ####################################
    def __init__(self):
        self.tabuleiro = np.zeros(shape = (8,8), dtype = int)
        self.rainhas = np.zeros(shape = (4, 2), dtype = int)
        
        
        #inicializando as rainhas
        self.rainhas[0][0] = self.rand07()
        self.rainhas[0][1] = self.rand07()
        
        aux = 1;
        
        while(True):
            x = self.rand07()
            y = self.rand07()
            
            if not ([x,y] in self.rainhas.tolist()):
                self.rainhas[aux][0] = x
                self.rainhas[aux][1] = y
                
                aux += 1               
                
            if aux == 4:
                break
            
        #colocando as rainhas no tabuleiro
        for i in range(4):
            x = self.rainhas[i][0]
            y = self.rainhas[i][1]
            self.tabuleiro[x][y] = 1
        
    #########################################################################
            
    def rand07(self):
        return randint(0, 7)
        
    def hasConflito(self, x, y):
        return (self.checkHorizontal(x, y) == False and self.checkVertical(x, y) == False and self.checkDiagonalPositivo(x, y) == False and self.checkDiagonalNegativo(x, y) == False)
    
    
    def checkBorderRight(self, value):
        if value == 8:
            return 0
        return value
        
    def checkBorderLeft(self, value):
        if value == -1:
            return 8
        return value
    
    def checkHorizontal(self, x, y):
        print('buscando na horizontal')
        aux = x
        auy = y
        for i in range(7):
            aux += 1
            aux = self.checkBorderRight(aux)
            
            print('x: ' + str(aux) + ' y: ' + str(auy))
            
            if (self.tabuleiro[aux][auy] == 1) and (aux is not x):
                return True
        return False
    
    def checkVertical(self, x, y):
        print('buscando na vertical')
        auy = y
        aux = x
        for i in range(7):
            auy += 1
            auy = self.checkBorderRight(auy)
            print('x: ' + str(aux) + ' y: ' + str(auy))
            
            if (self.tabuleiro[aux][auy] == 1) and (auy is not y):
                return True
        return False
            
    def checkDiagonalPositivo(self, x, y):
        print('buscando na diagonal positiva')
        auy = y
        aux = x
        for i in range(7):
            aux += 1
            auy += 1
            
            
            #chegou a borda em y
            if auy == 8:
                auy = 8 - aux
                aux = 0
            #chegou a borda em x
            if aux == 8:
                aux = 8 - auy
                auy = 0
                
            #chegou na mesma peça
            if (aux == x) and (auy == y):
                break
        
            print('x: ' + str(aux) + ' y: ' + str(auy))
            
            if self.tabuleiro[aux][auy] == 1:
                return True
            
        return False
        
        
    def checkDiagonalNegativo(self, x, y):
        print('buscando na diagonal negativa')
        auy = y
        aux = x
        for i in range(7):
            aux += 1
            auy -= 1
            
            if auy == -1:
                auy = aux - 1
                aux = 0
                
            if aux == 8:
                aux = auy + 1
                auy = 7
            #chegou na mesma peça
            if (aux == x) and (auy == y):
                break
                    
            print('x: ' + str(aux) + ' y: ' + str(auy))
                    
            if self.tabuleiro[aux][auy] == 1:
                return True
            
        return False
        
    
jogo = Jogo()
jogo.initRainhas()
