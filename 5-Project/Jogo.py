import numpy as np
from random import randint

class Jogo:
    ####################### CONSTRUTOR #########################
    def __init__(self):
        self.tabuleiro = np.zeros(shape = (8,8), dtype = int)
        self.rainhas = np.array([[-1, -1], [-1, -1], [-1, -1], [-1, -1]])

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
            
        self.totalPontuacao = self.pontuacao()
            
    ###########################################################
        
    # Printando o tabuleiro 
    # @return void

    def printJogo(self):
        for i in range(4):
            print('Rainha ' + str(i) + ' : ' + str(self.rainhas[i]))
            
        print()
        print(self.tabuleiro)
        print('A pontuação é de: ' + str(self.totalPontuacao))
        print()
        print('---------------------------------------')
            
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
    
    # Soma dos conflitos totais no jogo
    #    
    # @return int
    def pontuacao(self):
        count = 0
        for i in range(4):
            x = self.rainhas[i][0]
            y = self.rainhas[i][1]
            count += self.conflitoRainha(x, y)
            
        return count / 2
        
    
    # Faz os calculos de quantos conflitos uma peça no tabuleiro tem
    #    
    # @param int x          coord x
    # @param int y          coord y
    #    
    # @return soma dos conflitos
    def conflitoRainha(self, x, y):
        return (self.checkHorizontal(x, y) + self.checkVertical(x, y) + self.checkDiagonalPositivo(x, y) + self.checkDiagonalNegativo(x, y))
    
    # Conflito de borda positiva
    #    
    # @param int value
    #    
    # @return se ele chegou no conflito, ele retorna pra o 0
    def checkBorderRight(self, value):
        if value == 8:
            return 0
        return value
        
    # Conflito de borda negativa
    #    
    # @param int value
    #    
    # @return se ele chegou no conflito, ele retorna pra o 8
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
        
        countConflit = 0
        aux = x
        auy = y
        for i in range(7):
            aux += 1
            aux = self.checkBorderRight(aux)
            
            if (self.tabuleiro[aux][auy] == 1) and (aux is not x):
                countConflit += 1
        return countConflit
    
    # Contagem de quantos conflitos existem na vertical
    #    
    # @param int x          coord x
    # @param int y          coord y
    #    
    # @return int count conflitos
    def checkVertical(self, x, y):
        countConflit = 0
        auy = y
        aux = x
        for i in range(7):
            auy += 1
            auy = self.checkBorderRight(auy)

            if (self.tabuleiro[aux][auy] == 1) and (auy is not y):
                countConflit += 1
        return countConflit
    
    # Contagem de quantos conflitos existem na diagonal positiva
    #    
    # @param int x          coord x
    # @param int y          coord y
    #    
    # @return int count conflitos            
    def checkDiagonalPositivo(self, x, y):
        countConflit = 0
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
            
            if self.tabuleiro[aux][auy] == 1:
                countConflit += 1
            
        return countConflit
        
    # Contagem de quantos conflitos existem na diagonal negativa
    #    
    # @param int x          coord x
    # @param int y          coord y
    #    
    # @return int count conflitos        
    def checkDiagonalNegativo(self, x, y):
        countConflit = 0
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
                    
            if self.tabuleiro[aux][auy] == 1:
                countConflit += 1
            
        return countConflit
    
    def getTabuleiro(self):
        return self.tabuleiro
    
    # Mutação de uma das rainhas
    #    
    # @return void
    
    def mutacao(self):
        #Escolhendo uma das 4 rainhas para fazer a mutação
        indexRainha = randint(0, 3)
        
        antigoX = self.rainhas[indexRainha][0]
        antigoY = self.rainhas[indexRainha][1]
        
        #Escolhendo a nova posição dessa rainha
        novoX = self.rand07()
        novoY = self.rand07()
        
        #caso a posição que ele escolheu já esteja ocupada
        while True:
            if self.isEspacoOcupado(novoX, novoY):
                novoX = self.rand07()
                novoY = self.rand07()                
            else: 
                break;
                          
        print('Swaping Rainha ' + str(indexRainha) + ' [' + str(antigoX) + ',' + str(antigoY) + ']')
        print('Para a posição: ' + ' [' + str(novoX) + ',' + str(novoY) + ']')
        print('========================')
        
        #Trocando na referencia das rainhas
        self.rainhas[indexRainha][0] = novoX
        self.rainhas[indexRainha][1] = novoY
        
        #Fazendo a troca no tabuleiro
        self.tabuleiro[antigoX][antigoY] = 0
        self.tabuleiro[novoX][novoY] = 1
        
        self.totalPontuacao = self.pontuacao()