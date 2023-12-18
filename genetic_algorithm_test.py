#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from genetic_algorithm import GeneticAlgorithm


# objective function
def onemax(x):
    return -sum(x)


def alternator(x):
    x = [y - 0.5 for y in x]
    return abs(sum(x))


# define the total iterations
n_iter = 100
# bits - Increased to 30, rather than 20. This allows for longer prompts, However, not too long.
n_bits = 30
# define the population size
n_pop = 100
# crossover rate
r_cross = 0.9
# mutation rate
r_mut = 1.0 / float(n_bits)
# probability of doing a single point or double point crossover
r_point = 0.5

# perform the genetic algorithm search
best, score = GeneticAlgorithm.genetic_algorithm(onemax,
                                                 n_bits,
                                                 n_iter,
                                                 n_pop,
                                                 r_cross,
                                                 r_mut,
                                                 r_point)
print('Done!')
print('f(%s) = %f' % (best, score))