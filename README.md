# AI-Hackathon - Project Continued: Enhancing Prompts to Improve Accuracy.

## Quick Definitions: 
What is an LLM?

A Large Language Model is an advanced artificial intelligence model designed to process and generate human-like text. These models, such as OpenAI's GPT-3.5, have been trained on a vast amount of internet text to learn patterns, grammar, and factual information.

What are genetic algorithms?

In the context of using Large Language Models (LLMs) to engineer prompts, a genetic algorithm (GA) can be employed as a method for optimizing or evolving prompts to achieve specific objectives. 
## Step 1: Define the problem our project is solving:
In this case, the goal is to enhance the prompts used for a language model to improve the accuracy and context relevance of its responses.
## Step 2: Understand the Current System
The Current Large Language Model this project is using is Mistral AI (a.k.a Mistralai). 

- It is a pre-trained Deep Learning model (Meaning that it has been trained on large datasets to accomplish a specific task already.)

- Even though it is a pre-trained model, it can be used without modifying it or, if needed, customized to suit application requirements across industries (Accounting, healthcare etc.)
### About the LLM
- Mistral 7B v0.1 is a 7-billion-parameter language model focused on superior performance and efficiency.

- Mistral 7B outperforms Llama 2 13B in all evaluated benchmarks and surpasses Llama 1 34B in reasoning, mathematics, and code generation.

- The model incorporates grouped-query attention (GQA) for faster inference and sliding window attention (SWA) to handle sequences of arbitrary length efficiently and with reduced inference cost.

- What does Inference mean?
Inference refers to the process of generating predictions or responses based on a trained language model. 

Once a language model, such as Mistral AI LLM, has been trained on a dataset and has learned patterns and relationships within the data, inference involves using hte model to make predictions or generate text given a new input. 

Once the program performs inference (generating text given a new input), the language model evaluates the fitness of the generated prompts or sequences. This helps assess the quality of the generated prompts.

- What does grouped-query attention (GQA) mean?

Grouped Query Attention (GQA) is a mechanism used in language models, particularly in the context of attention mechanisms in neural networks. To understand GQA, we must break it down.

 1. What are attention mechanisms?
 In neural networks, especially in natural language processing tasks, attention mechanisms are used to focus on different parts of the input sequence when generating an output (E.g An attention mechanism will help the model focus on the most relevant words of the prompt. This improves the context-awareness of the model before generating an output.)


2. What is Grouped Query Attention (GQA)?
GQA is an specific type or modification of attention mechanisms. It's purpose is to improve the efficiency of attention computations during the inference phase.

- How does it work?
It groups queries (typically tokens or words) in a way that allows the model to attend to them collectively. This reduces the computational cost of attending to individual queries independently.

For example, without GQA - Attention mechanism attends to each word within the prompt individually.

Prompt: "Evolve prompts for a chatbot"
Attention: [0.1, 0.05, 0.2, 0.8] #Higher attention on chatbot

The attention spread is spread across individual words, with a higher weight on "chatbot" - context of prompt.

With GQA - Attention mechanisms groups queries / words together, resulting in attention being efficiently processed in the prompt.

Prompt: "Evolve prompts for a chatbot"
Attention: [0.3, 0.4, 0.3]

Using GQA, the queries are grouped together and for efficient processing:

Attention Spread breakdown

"Evolve prompts for a" Group
- Query: "Evolve prompts for a"
- Attention weight: 0.3 (hypothetical value)

"Chatbot" group
- Attention Weight: 0.4 (hypothetical value)
- Attention weight is higher. This due to the context value of the query

Remaining Attention (0.3)
- This could represent the attention assigned to the remaining context or words in the prompt that are not part of a grouped query. It is necessary as it ensures that the attention weight sums to 1, reflecting the entire prompt.


- What does sliding window attention (SWA) mean?

## Step 3: Define Fitness Function
Create a fitness function that evaluates the quality of a prompt and its corresponding response. The fitness function should quantify how well the language model performs based on the given prompt. For example, you can consider factors like relevance, correctness, and coherence.

## Step 4: Define Genetic Representation
Represent prompts as bitstrings. Each bit in the bitstring corresponds to a specific aspect or token in the prompt. Define a mapping that translates bitstrings into actual prompts that the language model can understand.

## Step 5: Implement the Genetic Algorithm
Use the provided genetic algorithm as a template. Integrate it with your language model and fitness function. Customize the genetic operations (crossover, mutation, insertion, deletion) to manipulate prompts effectively.

## Step 6: Initialization
Create an initial population of prompts (bitstrings). These prompts can be randomly generated or based on your domain knowledge. Ensure diversity in the initial population.

## Step 7: Evolution Loop
Run the genetic algorithm through multiple generations. In each generation:

Evaluate the fitness of each prompt-response pair using the defined fitness function.
Select the top-performing prompts based on fitness scores.
Apply genetic operations (crossover, mutation, insertion, deletion) to create a new generation of prompts.
Introduce new, random prompts for diversity.

## Step 8: Evaluate and Iterate
After the specified number of generations, evaluate the final population of prompts. Identify the prompts with the highest fitness scores. Test these optimized prompts with your language model.

If the performance is satisfactory, you've successfully enhanced the prompts. If not, consider refining the fitness function or adjusting genetic algorithm parameters, and repeat the process.

## Step 9: Results Analysis
Analyze the responses generated using the optimized prompts. Compare them with the initial responses to assess the improvement. Use qualitative and quantitative metrics to measure success.

## Step 10: Documentation and Deployment
Document the entire process, including the problem definition, algorithm parameters, and results. If the enhanced prompts yield significant improvements, deploy the optimized prompts in your language model for real-world applications.

### Important Note: Customize the steps based on your language model
Remember to customize the steps based on the specific characteristics and requirements of your language model and conversational AI system.






