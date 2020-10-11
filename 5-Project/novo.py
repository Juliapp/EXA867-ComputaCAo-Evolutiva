import numpy as np

class Jogo:
    def __init__(self):
        self.tabuleiro = np.zeros(shape = (8,8), dtype = int)
        
        
        
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
            

            #chegou na mesma peça
 
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
jogo.hasConflito(1, 7)
