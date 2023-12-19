# AI-Hackathon

Quick Definitions: 

What is an LLM?

A Large Language Model is an advanced artificial intelligence model designed to process and generate human-like text. Similar to ChatGPT 3.5.

What are genetic algorithms?

In the context of using Large Language Models (LLMs) to engineer prompts, a genetic algorithm (GA) can be employed as a method for optimizing or evolving prompts to achieve specific objectives. In our case, we are evolving prompts to produce outputs that are similar to the provided target output. (Contained within a csv file)

Ok, so what is the goal of our project?

The goal of our project is to create a genetic algorithm to reverse engineer an effective prompt to an LLM (Large Language Model) This prompt must produce outputs similar to the supplied desired output.
(Note: Scott has found a dataset that contains the desired output for each prompt. Therefore, the desired output is supplied.)

Project Requirements

1. Determine the kind of output that you want to engineer a prompt for (this should be a solution to some simple practical problem)

2. Determine how to encode the prompts so that the genetic algorithm can be applied

3. Determine how to calculate the fitness of a prompt, based on some measure of how well the LLM output generated from the prompt solves the simple practical problem.

4. Keep in mind that this will require making calls to the LLM to evaluate the fitness, so you will need to be mindful of how to optimize this computation to make it feasible to run the genetic algorithm.

To achieve these goals effectively, the focus is on:

- How to adequately represent the solution space (the set of prompts)

- How to measure the fitness of solutions (including how good a prompt is at generating output similar to the target)

- How to optimize the performance of the genetic algorithm.

Progress so far:

As a starting point, we're using the workshop example that generates prompts which will be transformed into a set of words. These sets of words will be used as a prompt and passed on to an LLM. Through evolution & natural selection methods, the prompt that produces an output most similar to the desired output will be selected and displayed.

How the prompts are generated:

# Step 1: Initialization
## 1.1. Population Initialization:

Generate a population (pop) of individuals, where each individual is represented as a random binary bitstring. E.g [0,1,1,1,1,0,1] The length of each bitstring is determined by n_bits. After evolution, the most effective individuals will be converted into strings and passed onto an LLM as prompts. The prompts which produces an output similar to the desired output (supplied) wins the selection phase.

Code Snippit of Population Initialisation phase:
E.g Initializing the population with random bitstrings
pop = [randint(0, 2, n_bits).tolist() for _ in range(n_pop)]

## 1.2. Best Solution Tracking:
To keep track of the best solution (that will produce an output similar to the desired output) and it's evaluation / fitness score within the population, the variables best and best_eval are intialised. The best variable is set to 0 intially, and the best_eval is set to the evaluation of the first individual in the population.

Code Snippit of Population Best Solution Tracking phase:
E.g Keeps track of the best solution and its evaluation
best, best_eval = 0, objective(pop[0])

# Step 2: Iterative Generation Loop
## 2.1. Evaluation of Fitness:

Evaluate the fitness of each individual in the population using the objective function.
## 2.2. Update Best Solution:

If the fitness of an individual is better than the current best solution, update best and best_eval with the new individual's values and print the information.
## 2.3. Parent Selection:

Use tournament selection (_selection function) to choose parents for the next generation. The selected parents are stored in the selected list.
## 2.4. Crossover and Mutation:

For each pair of parents, apply crossover and mutation operations to generate two children. The crossover operation is based on probabilities (r_cross, r_point, r_ins, r_del), and the children are stored in the children list.
## 2.5. Replace Population:

Replace the current population with the new children.
# Step 3: Termination
## 3.1. Iterations:

Repeat the generation loop for a specified number of iterations (n_iter).
# Step 4: Return Best Solution
## 4.1. Return:

Return a list containing the best solution (best) and its evaluation (best_eval) after the specified number of generations.
# Additional Functions
## _selection Function:

Implements tournament selection to choose parents based on fitness scores.
## _crossover Function:

Performs crossover between two parents based on probabilities and generates two children.
## _insertion and _deletion Functions:

Perform random bit insertion and deletion on a given bitstring.
## _mutation Function:

Mutates a bitstring based on a mutation rate.
