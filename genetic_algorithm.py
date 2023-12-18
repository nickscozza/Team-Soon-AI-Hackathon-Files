#Header Section:
#Path to the Python 3 Interpreter
#!/usr/bin/env python3
#Encoding Declaration (utf-8)
# -*- coding: utf-8 -*-
#Acknowledgment
#Source: https://machinelearningmastery.com/simple-genetic-algorithm-from-scratch-in-python/

#IMPORTANT: Most of this code looks abnormal / strange due to experimentation with chatgpt.
#By 18/12/23, it will be massively modifed to make sense. Thanks for your patience.

#Import Section:
#rand() and random() are functions to import random floating-point numbers between 0 and 1
#Useful for setting probability measures.
from numpy.random import rand, random

#randint(low, high) is a function that generates an random integer between 'low' (inclusive) and 'high' (exclusive).
#Useful for tasks like randomly initializing the genetic material (bitstrings) in the population

from numpy.random import randint
#randrange(start, stop) is a function that generates an random integer between a range ('start' (inclusive) and 'stop' (exclusive) )
#Useful for determining a crossover point during the genetic crossover operation (where genetic material is exchanged between 2 parents)
from random import randrange

#Main Code section:
# genetic algorithm
#
# genetic algorithm
class GeneticAlgorithm():

    @classmethod
    def genetic_algorithm(cls, objective, n_bits, n_iter, n_pop, r_cross, r_mut):
        # initial population of random bitstring
        pop = [randint(0, 2, n_bits).tolist() for _ in range(n_pop)]
        # keep track of best solution
        best, best_eval = 0, objective(pop[0])
        # enumerate generations
        for gen in range(n_iter):
            # evaluate the fitness of all candidates in the population
            scores = [objective(c) for c in pop]
            # check for new best solution
            for i in range(n_pop):
                if scores[i] < best_eval:
                    best, best_eval = pop[i], scores[i]
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
    def _crossover(cls, p1, p2, r_cross):
        # children are copies of parents by default
        c1, c2 = p1.copy(), p2.copy()
        # check for recombination
        if rand() < r_cross:
            # select crossover point that is not on the end of the string
            pt = randint(1, len(p1) - 2)
            # perform crossover
            c1 = p1[:pt] + p2[pt:]
            c2 = p2[:pt] + p1[pt:]
        return [c1, c2]

    @classmethod
    def _mutation(cls, bitstring, r_mut):
        for i in range(len(bitstring)):
            # check for a mutation
            if rand() < r_mut:
                # flip the bit
                bitstring[i] = 1 - bitstring[i]
