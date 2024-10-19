

This project is an experiment that simulates conversations between characters (I did this experiment for **a boyfriend and a girlfriend**)—by using Retrieval-Augmented Generation (RAG). The goal is to observe how the predefined behaviors of the characters influence their dialogues based on the knowledge base provided.

## Overview

RAG is a powerful approach that combines the strengths of retrieval systems with generative models to produce coherent and contextually relevant text. In this project, the knowledge base defines specific behaviors for each character, allowing them to engage in dynamic conversations. The experiment aims to explore how these behaviors manifest in their interactions.

## Key Features

- **Character Behaviors**: Each character (boyfriend and girlfriend) has a predefined set of behaviors and personality traits, which drive their conversation.
- **Dynamic Conversation**: The dialogue between characters changes based on the behavior and context retrieved from the knowledge base.
- **Retrieval-Augmented Generation (RAG)**: Combines retrieval from a knowledge base and text generation to create contextual and coherent dialogues.
- **Behavior Simulation**: The knowledge base is curated with scenarios, preferences, and responses tailored to each character’s behavior.

## How It Works

1. **Define Knowledge Base**: A knowledge base is created with behaviors and traits for each character.
2. **Run the Model**: The RAG system retrieves relevant behaviors from the knowledge base and generates context-aware responses for each character during the conversation.
3. **Observe Interaction**: The characters engage in dialogue based on the retrieved behaviors and generate natural, evolving conversations.

## Technologies Used

- **Python**: Core language for implementation.
- **RAG**: for RAG I have used llamaindex and ollama llms .
- **Embed Model**: The Embed model used here is BAAI/bge-base-en.
## Setup and Installation



- You need to have Ollama running first visit https://ollama.com/download to download and install ollama 
- For this project I have used llama3 model, you can use your any model you like.
    ```bash
	   ollama pull <model_name> 
    ```




- Clone the repository:
    ```bash
    git clone https://github.com/yourusername/character-interaction-rag.git
    cd Pseudo_Talk
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the main.py file to observe the conversation between two characters or you can run talk_to_character.py to talk with the character you wish:
    ```bash
    python main.py
        or
    python talk_to_character.py
    ```

## Customizing the Knowledge Base

You can modify the characters' behaviors by editing the `charater.txt` files. This file contains the predefined traits, preferences, and responses for each character. Adjusting these values will change the way the characters interact with each other.

## Future Work

- Expand the knowledge base with more diverse behaviors and scenarios.
- Introduce more characters and observe multi-character conversations.
- Improve the retrieval process to make responses more nuanced and personalized.



