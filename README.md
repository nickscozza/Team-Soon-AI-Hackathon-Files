Quick Definitions:
What is an LLM?

A Large Language Model is an advanced artificial intelligence model designed to process and generate human-like text. These models, such as OpenAI's GPT-3.5, have been trained on a vast amount of internet text to learn patterns, grammar, and factual information.

What are genetic algorithms?

In the context of using Large Language Models (LLMs) to engineer prompts, a genetic algorithm (GA) can be employed as a method for optimizing or evolving prompts to achieve specific objectives.

Ok, so what is the goal of our project?

The goal of our project is to create a genetic algorithm to reverse engineer an effective prompt to an LLM (Large Language Model) that will cause the LLM to generate output similar to a supplied target output.

Project Requirements

Determine the kind of output that you want to engineer a prompt for (this should be a solution to some simple practical problem)

Determine how to encode the prompts so that the genetic algorithm can be applied

Determine how to calculate the fitness of a prompt, based on some measure of how well the LLM output generated from the prompt solves the simple practical problem.

Keep in mind that this will require making calls to the LLM to evaluate the fitness, so you will need to be mindful of how to optimize this computation to make it feasible to run the genetic algorithm.

To achieve these goals effectively, the focus is on:

How to adequately represent the solution space (the set of prompts)

How to measure the fitness of solutions (including how good a prompt is at generating output similar to the target)

How to optimize the performance of the genetic algorithm.

As a starting point, we're using the workshop example that generates prompts. Initially, these prompts are in the form of binary genotypes (a.k.a binary lists). [0,1,1,0,1] etc.

To determine the fitness / similarity of the prompt, the binary genotype is first converted into a phenotype (as the output). the type of phenotype can be determined by the team, however an example is an set of adjectives.

Once provided to an LLM, the fitness of the prompt is based on the similarity of the output generated (Phenotype) when compared with the target output.

The objective of the program is to generate then specify prompts that when provided to the LLM, generate outputs that are similar to the target output.

To discover prompts that are effective in guiding the LLM to produce output (phenotypes) which is similar to the desired output, the program utilizes an genetic algorithm.

The genetic algorithm operates on binary genotypes, performing operations such as crossover and mutation to explore the space of possible prompts.

No LLM Call in Example:

It's important to note that in the given example, there is no direct call to the LLM. The output is the same as the prompt, and the sentiment similarity is computed based on the generated set of adjectives.

In our project, we will be making a direct call to the LLM. Therefore, will be able to evaluate the fitness score / similarity of the outputs generated.

To also help explain the process of genetic algorithms, here is an explanation:

Representation of Prompts:
In the context of prompt engineering, a prompt can be represented as a sequence of tokens or words.

Initialization:
The process starts with an initial population of prompts. Each prompt in the population is a potential candidate for generating desirable outputs from the LLM.

Evaluation:
The prompts in the population are fed into the LLM, and the resulting outputs are evaluated based on certain criteria or objectives. This could involve measuring the relevance, informativeness, or other qualities of the generated text. As a group, we need to determine the criteria that our prompt needs to satisfy. E.g the problem we're trying to solve.

Selection:
Prompts that lead to more desirable outputs are selected to be parents for the next generation. The selection process is influenced by the fitness / evaluation scores achieved.

Crossover (Recombination):
Pairs of the selected prompts are combined to create new prompts through a process called crossover or recombination. This mimics the idea of genetic crossover, where genetic material is exchanged between parents.

Mutation:
Some prompts in the new generation undergo mutation, introducing small random changes. This introduces exploration and prevents the algorithm from getting stuck in local optima.

Replacement:
The new generation of prompts replaces the old one, forming the next population.

Repeat:
Steps 3-7 are repeated for multiple generations, allowing the prompts to evolve over time. Once the prompts are most similar to the desired output, the process ends.






