# AI-Hackathon

Quick Definitions: 

What is an LLM?

A Large Language Model is an advanced artificial intelligence model designed to process and generate human-like text. These models, such as OpenAI's GPT-3.5, have been trained on a vast amount of internet text to learn patterns, grammar, and factual information.

What are genetic algorithms?

In the context of using Large Language Models (LLMs) to engineer prompts, a genetic algorithm (GA) can be employed as a method for optimizing or evolving prompts to achieve specific objectives. In our case, we are evolving prompts to produce outputs that are similar to the provided target output.

Ok, so what is the goal of our project?

The goal of our project is to create a genetic algorithm to reverse engineer an effective prompt to an LLM (Large Language Model) This prompt must produce outputs similar to the desired output.
(Note: Scott has found a dataset that contains the desired output for each prompt. Therefor)

Project Requirements

1. Determine the kind of output that you want to engineer a prompt for (this should be a solution to some simple practical problem)

2. Determine how to encode the prompts so that the genetic algorithm can be applied

3. Determine how to calculate the fitness of a prompt, based on some measure of how well the LLM output generated from the prompt solves the simple practical problem.

4. Keep in mind that this will require making calls to the LLM to evaluate the fitness, so you will need to be mindful of how to optimize this computation to make it feasible to run the genetic algorithm.

To achieve these goals effectively, the focus is on:

- How to adequately represent the solution space (the set of prompts)

- How to measure the fitness of solutions (including how good a prompt is at generating output similar to the target)

- How to optimize the performance of the genetic algorithm.

As a starting point, we're using the workshop example that generates prompts which are in the form of a set of words. These sets of words will be evoloved to produce an output that will be similar to an supplied desired output. 

The genetic algorithm operates on binary genotypes, performing operations such as crossover and mutation to explore the space of possible prompts & experiment with solutions.

By executing the genetic algorithm, we are able to evolve, manipulate, and select prompts that produce outputs similar to the desired output.
