import numpy as np
from random import randint

class Jogo:
    ####################### CONSTRUTOR #########################
    def __init__(self):
        self.tabuleiro = np.zeros(shape = (8,8), dtype = int)
        self.rainhas = np.array([[-1, -1], [-1, -1], [-1, -1]])

        #Inicializando as rainhas com tratamento de erro caso o random sortear 
        #a mesma posição mais de uma vez
        aux = 0;
        while(True):
            x = self.rand07()
            y = self.rand07()
            
            if not self.isEspacoOcupado(x, y):
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
            
    ###########################################################
        
    # Printando o tabuleiro 
    # @return void

    def printJogo(self):
        for i in range(4):
            print('Rainha ' + str(i) + ' : ' + str(self.rainhas[i]))
            
        print(self.tabuleiro)
            
    # Escolhe um inteiro entre 0 e 7
    # @return inteiro escolhido
    def rand07(self):
        return randint(0, 7)
    
    # Checa se o espaço passado por parametro já está sendo ocupado por uma rainha
    #    
    # @param int x          coord x
    # @param int y          coord y
    #    
    # @return True se já esta ocupado
    
    def isEspacoOcupado(self, x, y):
        return [x,y] in self.rainhas.tolist()
        
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
    
    # Contagem de quantos conflitos existem na horizontal
    #    
    # @param int x          coord x
    # @param int y          coord y
    #    
    # @return int count conflitos
    def checkHorizontal(self, x, y):
        aux = x
        auy = y
        for i in range(7):
            aux += 1
            aux = self.checkBorderRight(aux)
            
            print('x: ' + str(aux) + ' y: ' + str(auy))
            
            if (self.tabuleiro[aux][auy] == 1) and (aux is not x):
                return True
        return False
    
    # Contagem de quantos conflitos existem na vertical
    #    
    # @param int x          coord x
    # @param int y          coord y
    #    
    # @return int count conflitos
    def checkVertical(self, x, y):
        auy = y
        aux = x
        for i in range(7):
            auy += 1
            auy = self.checkBorderRight(auy)
            print('x: ' + str(aux) + ' y: ' + str(auy))
            
            if (self.tabuleiro[aux][auy] == 1) and (auy is not y):
                return True
        return False
    
    # Contagem de quantos conflitos existem na diagonal positiva
    #    
    # @param int x          coord x
    # @param int y          coord y
    #    
    # @return int count conflitos            
    def checkDiagonalPositivo(self, x, y):
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
        
    # Contagem de quantos conflitos existem na diagonal negativa
    #    
    # @param int x          coord x
    # @param int y          coord y
    #    
    # @return int count conflitos        
    def checkDiagonalNegativo(self, x, y):
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
