from utils.nodes_generator import NodeGenerator
from algorithms.simulated_annealing import SimulatedAnnealing


def main():
    #set the simulated annealing algorithm params
    temp = 1000
    stopping_temp = 0.00000001
    alpha = 0.999777
    stopping_iter = 100000

    #set the dimensions of the grid
    size_width = 200
    size_height = 200

    #cities to visit
    population_size = 1000

    #generate random list of nodes in the grid
    nodes = NodeGenerator(size_width, size_height, population_size).generate()

    '''run simulated annealing algorithm with 2-opt'''
    sa = SimulatedAnnealing(nodes, temp, alpha, stopping_temp, stopping_iter)
    sa.anneal()

    '''animate'''
    sa.animateSolutions()

    '''show the improvement over time'''
    sa.plotLearning()


if __name__ == "__main__":
    main()