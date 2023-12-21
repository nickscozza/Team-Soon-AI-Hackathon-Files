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

from numpy.random import rand, random
#randint(low, high) is a function that generates an random integer between 'low' (inclusive) and 'high' (exclusive).
#Useful for tasks like randomly initializing the genetic material (bitstrings) in the population


from numpy.random import randint
#randint(low, high) is a function that generates an random integer between 'low' (inclusive) and 'high' (exclusive).
#Useful for tasks like randomly initializing the genetic material (bitstrings) in the population

from random import randrange
#randrange(start, stop) is a function that generates an random integer between a range ('start' (inclusive) and 'stop' (exclusive) )
#Useful for determining a crossover point during the genetic crossover operation (where genetic material is exchanged between 2 parents)

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
    #r_cross = Crossover rate, determining the probability of an crossover occurring
    #r_mut = mutation rate, determining the probability of mutation occurring.
    #r_point = probability of performing a single or double crossover
    
    def genetic_algorithm(cls, objective, n_bits, n_iter, n_pop, r_cross, r_mut, r_point, r_ins, r_del):
        
        #initializing the pop (population) with random bitstrings
        pop = [randint(0, 2, n_bits).tolist() for _ in range(n_pop)]
        #randint(0, 2, n_bits) generates a random binary array of the length stored inside of n_bits
        #.tolist() converts the array into a python list. Arrays are generated until the n_pop value is reached.
        
        #Keeps track of the best solution and it's evaluation in the variable 'best' and 'best_eval'.
        best, best_eval = 0, objective(pop[0])
        #best is set to 0 initially, and best_eval is set to the evaluation / fitness score of the first individual in the population        
        
        #Generation loop: For the each generation,
        #loop until reaching the max number of iterations (0 to n_iter - 1)
        for gen in range(n_iter):
            # evaluate the fitness of all candidates in the population using the 'objective' function
            scores = [objective(c) for c in pop]
            
            # check for new best solution
            #Evaluates the fitness of all individuals in the population using the 'objective' function
            for i in range(n_pop):
                if scores[i] < best_eval:
                    best, best_eval = pop[i], scores[i]
                    #Whenever the next best solution is found, it is printed.
                    print(">%d, new best f(%s) = %.3f" % (gen, pop[i], scores[i]))
            
            # select parents based on tournament selection (using _selection function)
            selected = [cls._selection(pop, scores) for _ in range(n_pop)]
            #This line is creating a list of 'selected' candidates for the next generation 
            #by repeatedly applying the tournament selection process.
            #it is executed for each iteration of 'n_pop'
            
            #Create the next generation - this generation will be converted to a list.
            children = list()
            
            #for in range (0 to population, incrementing by 2)
            for i in range(0, n_pop, 2):
                
                #Store 2 children inside of p1 and p2 (using the index inside of the selected list)
                p1, p2 = selected[i], selected[i + 1]
                
                #Crossover and Mutation
                for c in cls._crossover(p1, p2, r_cross, r_point, r_ins, r_del):
                    # mutation
                    cls._mutation(c, r_mut)
                    # store for next generation inside of the children list
                    children.append(c)
            # replace population with the children list
            pop = children
        #Returns a list containing the best solution 'best' and its evaluation 'best_eval' after a specified number of generations
        return [best, best_eval]

    @classmethod
    #A function that selects parents based on tournament selection
    def _selection(cls, pop, scores, k=3):
        #k = number of individuals in tournament (which is set to 3)
        #pop = current population of individuals. Each individual is represented as a bitstring.
        #scores = evaluation scores
        
        # first random selection
        selection_x = randint(len(pop))
        for x in randint(0, len(pop), k - 1):
            # check if better (e.g. perform a tournament)
            if scores[x] < scores[selection_x]:
                selection_x = x
        return pop[selection_x]

    @classmethod
    def _insertion(cls, bitstring):
        """
        Insert a random bit on the given bitstring.

        Parameters:
        - bitstring (list): bitstring to mutate
        """
        i = randint(len(bitstring))
        if bitstring[i] == 1:
            bitstring[i] = 0
        else:
            bitstring[i] = 1

    @classmethod
    def _deletion(cls, bitstring):
        """
        Delete a random bit on the given bitstring
        
        Parameters:
        - bitstring (list): bitstring to mutate
        """
        del bitstring[randint(len(bitstring))]

    @classmethod
    #A crossover function that performs a crossover between 2 parents.
    #Based on the r_cross probability, it checks if a crossover will occur.
    def _crossover(cls, p1, p2, r_cross, r_point, r_ins, r_del):

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
        
            # possibly perform insertions on children
            if rand() < r_ins:
                cls._insertion(c1)
            if rand() < r_ins:
                cls._insertion(c2)

            # possibly perform deletions on children
            if len(c1) > 1 and rand() < r_del:
                cls._deletion(c1)
            if len(c2) > 1 and rand() < r_del:
                cls._deletion(c2)

        return [c1, c2]

    @classmethod
    #A function that mutates a bi-string based on mutation rate.
    def _mutation(cls, bitstring, r_mut):
        for i in range(len(bitstring)):
            # check for a mutation
            if rand() < r_mut:
                # flip the bit
                bitstring[i] = 1 - bitstring[i]
