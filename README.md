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

As a starting point, we're using the workshop example that generates prompts which will be transformed into a set of words. These sets of words will be used as a prompt and passed on to an LLM. Through evolution & natural selection methods, the prompt that produces an output most similar to the desired output will be selected.

Initially, The genetic algorithm produces binary genotypes [0,1,1,0] as prompts. After generation, the algorithm will performing operation such as crossover and mutation to explore the space of possible prompts & experiment with combined genotypes. These genotypes will be converted into strings (which contains a set of words) 

Each time a binary genotype is produced & manipulated (some may not be manipulated), They will be evaluated through their ability to satisfy certain requirements (related to the desired output).

Whichever solution produces an output most similar to the supplied target output, will be selected at the end.
