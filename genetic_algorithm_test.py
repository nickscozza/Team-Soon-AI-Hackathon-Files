#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#IMPORTANT: Most of this code looks abnormal / strange due to experimentation with chatgpt. Therefore, disregard any code that does not make sense.
#By 10am 18/12/23, it will be massively modifed to make sense. Thanks for your patience.

from genetic_algorithm import GeneticAlgorithm


# objective function
def onemax(x):
    return -sum(x)


def alternator(x):
    x = [y - 0.5 for y in x]
    return abs(sum(x))


# define the total iterations
n_iter = 100
# bits
n_bits = 20
# define the population size
n_pop = 100
# crossover rate
r_cross = 0.9
# mutation rate
r_mut = 1.0 / float(n_bits)

# Insertion Rate
r_ins = 0.1

# Deletion Rate
r_del = 0.4

# perform the genetic algorithm search
best, score = GeneticAlgorithm.genetic_algorithm(onemax,
                                                 n_bits,
                                                 n_iter,
                                                 n_pop,
                                                 r_cross,
                                                 r_mut,
                                                 r_ins,
                                                 r_del)
print('Done!')
print('f(%s) = %f' % (best, score))
