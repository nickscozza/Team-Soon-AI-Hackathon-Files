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

# A In-Depth Explanation of how the Genetic Algorithm is executed

# Step 1: Initialization
## 1.1. Population Initialization:

Generate a population (pop) of individuals, where each individual is represented as a random binary bitstring. E.g [0,1,1,1,1,0,1] The length of each bitstring is determined by n_bits. After evolution, the most effective individuals will be converted into strings and passed onto an LLM as prompts. The prompts which produces an output similar to the desired output (supplied) wins the selection phase.

Code Snippit of Population Initialisation phase

	#Initializing the population with random bitstrings
	pop = [randint(0, 2, n_bits).tolist() for _ in range(n_pop)]

## 1.2. Best Solution Tracking:
To keep track of the best solution (that will produce an output similar to the desired output) and it's evaluation / fitness score within the population, the variables best and best_eval are intialised. 

Code Snippit of Population Best Solution Tracking phase:
		
	#Keeps track of the best solution and its evaluation
	best, best_eval = 0, objective(pop[0])

Note: The best variable is set to 0 intially, and the best_eval is set to the evaluation of the first individual in the population.

# Step 2: Iterative Generation Loop
## 2.1. Evaluation of Fitness (using the Objective() function:

Next, the fitness of each individual within the generated population is evaluated using the objective function.

Code Snippit of Objective function call:

	#Uses a for loop to evaluate the fitness scores of each individual inside the population.
	scores = [objective(c) for c in pop]

## 2.2. Update Best Solution:

If the fitness of an individual is better than the current best solution, update best and best_eval with the new individual's values and print the information.

Code Snippit:

	#Update the best solution if a new better solution is found
	for i in range(n_pop):
		if scores[i] < best_eval:
			best, best_eval = pop[i], scores[i]
			print(">%d, new best f(%s) = %.3f" % (gen, pop[i], scores[i]))

## 2.3. Parent Selection:

Use tournament selection (_selection function) to choose parents for the next generation. The selected parents are stored in the selected list.

Code Snippit:

	#Select parents based on tournament selection
 	selected = [cls._selection(pop, scores) for _ in range(n_pop)]

## 2.4. Crossover and Mutation:

For each pair of parents, apply crossover and mutation operations to generate two children. The crossover operation is based on probabilities (r_cross, r_point, r_ins, r_del), and the children are stored in the children list.

Code Snippit:

	#Create the next generation - crossover and mutation
	children = list()
	for i in range(0, n_pop, 2):
  		p1, p2 = selected[i], selected[i + 1]
  		for c in cls._crossover(p1, p2, r_cross, r_point, r_ins, r_del):
			cls._mutation(c, r_mut)
			children.append(c)


## 2.5. Replace Population:

Replace the current population with the new children.

Code Snippet:

	#Replace the population with the children by assigning children to it.
	pop = children


# Step 3: Termination
## 3.1. Iterations:

Repeat the generation loop for a specified number of iterations (n_iter).

Code Snippet:

	#Repeat the generation loop for a specified number of iterations
	for gen in range(n_iter):
 	<Steps 2.1 to 2.5 are repeated for a number of iterations>
    
# Step 4: Return Best Solution
## 4.1. Return:

Return a list containing the best solution (best) and its evaluation (best_eval) after the specified number of generations.

Code Snippet:

	#Return the best solution and its evaluation after a specified number of generations
	return [best, best_eval]


# Additional Functions
## _selection Function:

Implements tournament selection to choose parents based on fitness scores.

	@classmethod
	def _selection(cls, pop, scores, k=3):
    # Tournament selection
    selection_x = randint(len(pop))
    for x in randint(0, len(pop), k - 1):
        if scores[x] < scores[selection_x]:
            selection_x = x
    return pop[selection_x]

## _crossover Function:

Performs crossover between two parents based on probabilities and generates two children.

	@classmethod
	def _crossover(cls, p1, p2, r_cross, r_point, r_ins, r_del):
    # Crossover operation based on probabilities
    c1, c2 = p1.copy(), p2.copy()
    if rand() < r_cross:
        # Single or double-point crossover
        if rand() < r_point:
            single_point = randint(1, len(p1) - 1)
            c1 = p1[:single_point] + p2[single_point:]
            c2 = p2[:single_point] + p1[single_point:]
        else:
            double_point = np.sort(randint(1, len(p1) - 1, size=2))
            pt1, pt2 = double_point
            c1 = p1[:pt1] + p2[pt1:pt2] + p1[pt2:]
            c2 = p2[:pt1] + p1[pt1:pt2] + p2[pt2:]
        # Possibly perform insertions and deletions
        if rand() < r_ins:
            cls._insertion(c1)
        if rand() < r_ins:
            cls._insertion(c2)
        if len(c1) > 1 and rand() < r_del:
            cls._deletion(c1)
        if len(c2) > 1 and rand() < r_del:
            cls._deletion(c2)
    return [c1, c2]


## _insertion and _deletion Functions:

Perform random bit insertion and deletion on a given bitstring.

Insertion function:

 	@classmethod
 	def _insertion(cls, bitstring):
        i = randint(len(bitstring))
        if bitstring[i] == 1:
            bitstring[i] = 0
        else:
            bitstring[i] = 1

 Deletion Function:

    @classmethod
    def _deletion(cls, bitstring):
        """
        Delete a random bit on the given bitstring
        
        Parameters:
        - bitstring (list): bitstring to mutate
        """
        del bitstring[randint(len(bitstring))]

## _mutation Function:

Mutates a bitstring based on a mutation rate.

	@classmethod
	def _mutation(cls, bitstring, r_mut):
    # Mutation based on mutation rate
    for i in range(len(bitstring)):
        if rand() < r_mut:
            bitstring[i] = 1 - bitstring[i]

