#Header Section:
#Path to the Python 3 Interpreter
#!/usr/bin/env python3
#Encoding Declaration (utf-8)
# -*- coding: utf-8 -*-
#Acknowledgment
#Source: https://machinelearningmastery.com/simple-genetic-algorithm-from-scratch-in-python/

#Import Section:
import numpy as np

#rand() and random() are functions to import random floating-point numbers between 0 and 1
#Useful for setting probability measures.
from np.random import rand, random

#randint(low, high) is a function that generates an random integer between 'low' (inclusive) and 'high' (exclusive).
#Useful for tasks like randomly initializing the genetic material (bitstrings) in the population

from np.random import randint
#randrange(start, stop) is a function that generates an random integer between a range ('start' (inclusive) and 'stop' (exclusive) )
#Useful for determining a crossover point during the genetic crossover operation (where genetic material is exchanged between 2 parents)
from random import randrange

#Main Code section:
# genetic algorithm

class GeneticAlgorithm():

    @classmethod
    #@classmethod indicates that the following function is a class method, not an instance method.
    #Note: Class methods always take themselves as the first parameter, therefore "cls" represents the class itself.
    
    #Main function implementing the the genetic algorithm
    #Explanation of parameters
    #cls = the class parameter
    #Objective = A function that evaluates the fitness of the candidate solution
    #n_bits = The length of the the bitstrings representing individuals.
    #n_iter = the number of generations or iterations
    #n_pop = the size of the population
    #r_cross = Crossover rate, determining the probability of an crossover occuring
    #r_mut = mutation rate, determining the probability of mutation occuring.
    def genetic_algorithm(cls, objective, n_bits, n_iter, n_pop, r_cross, r_mut):
        #initializing the pop (population) with random bitstrings
        pop = [randint(0, 2, n_bits).tolist() for _ in range(n_pop)]
        
        #Keeps track of the best solution and it's evaluation in the variable 'best' and 'best_eval'.
        best, best_eval = 0, objective(pop[0])
        
        #Generation loop: Iterates over generations.
        #In each generation, the fitness is evaluated, parents are selected and the next generation is created.
        for gen in range(n_iter):
            # evaluate the fitness of all candidates in the population
            scores = [objective(c) for c in pop]
            # check for new best solution
            for i in range(n_pop):
                if scores[i] < best_eval:
                    best, best_eval = pop[i], scores[i]
                    
                    #Whenever the next best solution is found, it is printed.
                    print(">%d, new best f(%s) = %.3f" % (gen, pop[i], scores[i]))
            # select parents
            selected = [cls._selection(pop, scores) for _ in range(n_pop)]
            # create the next generation
            children = list()
            for i in range(0, n_pop, 2):
                # get selected parents in pairs
                p1, p2 = selected[i], selected[i + 1]
                # crossover and mutation
                for c in cls._crossover(p1, p2, r_cross):
                    # mutation
                    cls._mutation(c, r_mut)
                    # store for next generation
                    children.append(c)
            # replace population
            pop = children
        return [best, best_eval]

    @classmethod
    def _selection(cls, pop, scores, k=3):
        # first random selection
        selection_x = randint(len(pop))
        for x in randint(0, len(pop), k - 1):
            # check if better (e.g. perform a tournament)
            if scores[x] < scores[selection_x]:
                selection_x = x
        return pop[selection_x]

    @classmethod
    def _crossover(cls, p1, p2, r_cross, r_point=0.5):
        # children are copies of parents by default
        c1, c2 = p1.copy(), p2.copy()
        # check for recombination
        if rand() < r_cross:
            if rand() < r_point:
                # perform single-point crossover
                single_point = randint(1, len(p1) - 1)
                c1 = p1[:single_point] + p2[single_point:]
                c2 = p2[:single_point] + p1[single_point:]
            else:
                # perform double-point crossover
                double_point =  [0, 0]

                # choose two different points randomly
                while double_point[0] == double_point[1]:
                    double_point = randint(1, len(p1) - 1, size=2)
                
                # sort points, compare order
                double_point = np.sort(double_point)
                pt1, pt2 = double_point

                # crossover
                c1 = p1[:pt1] + p2[pt1:pt2] + p1[pt2:]
                c2 = p2[:pt1] + p1[pt1:pt2] + p2[pt2:]
        return [c1, c2]

    @classmethod
    def _mutation(cls, bitstring, r_mut):
        for i in range(len(bitstring)):
            # check for a mutation
            if rand() < r_mut:
                # flip the bit
                bitstring[i] = 1 - bitstring[i]
