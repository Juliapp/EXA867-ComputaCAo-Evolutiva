from Jogo import Jogo

class HillClimb:
    
    def __init__(self):
        self.jogo = Jogo()
        self.melhorPontuacao = self.jogo.totalPontuacao
        
    def run(self):
        print('JOGO INICIAL: ')
        self.jogo.printJogo()
        
        count = 0
        while(self.melhorPontuacao != 0):
            count += 1
            self.jogo.mutacao()
            self.jogo.printJogo()
            
            if self.jogo.totalPontuacao < self.melhorPontuacao:
                self.melhorPontuacao = self.jogo.totalPontuacao
                
        print('CONFLITO ENTRE RAINHAS SOLUCIONADO: ')
        print('Quantidade de iterações: ' + str(count))
        print()
        self.jogo.printJogo()
        
                
hill = HillClimb()
hill.run()