from utils.nodes_generator import NodeGenerator
from algorithms.simulated_annealing import SimulatedAnnealing
import numpy as np
import random
import time
"""
TODO:
Valutazione delle performance--> parametri simulated annealing (#iterazioni,alfa.temp)
10 istanze per entrambe le versioni del problema(istanza geometrica e istanza con i pesi) con n che varia
da 100,500,1000,1500. Le caratteristiche da valutare al variare dei parametri sono funzione obiettivo e tempo di esecuzione
"""

def main():
    #set the simulated annealing algorithm params
    temp = 2000
    stopping_temp = 0.00000001
    alpha = 0.9997777
    stopping_iter = 100000

    #set the dimensions of the grid
    size_width = 200
    size_height = 200

    #cities to visit
    population_size = 1000

    #generate random list of nodes in the grid
    # Fissa il seme del generatore di numeri casuali per riproducibilità
    seed_value = 42
    np.random.seed(seed_value)
    random.seed(seed_value)
    nodes = NodeGenerator(size_width, size_height, population_size).generate()

    '''run simulated annealing algorithm with 2-opt'''
    start_time = time.time()
    sa = SimulatedAnnealing(nodes, temp, alpha, stopping_temp, stopping_iter)
    sa.anneal()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tempo di esecuzione: {elapsed_time} secondi")
    '''animate'''
    sa.animateSolutions()

    '''show the improvement over time'''
    sa.plotLearning()


if __name__ == "__main__":
    main()