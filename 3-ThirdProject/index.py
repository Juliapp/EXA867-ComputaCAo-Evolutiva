from AlgoritmoGenetico import AlgoritmoGenetico

TAXA_CROSSOVER = 0
TAXA_MUTACAO = 0
GERACOES = 0
POPULACAO = 4

ag = AlgoritmoGenetico(TAXA_CROSSOVER, TAXA_MUTACAO, GERACOES, POPULACAO)
ag.executaAG()
ag.populacao.printPopulacao()