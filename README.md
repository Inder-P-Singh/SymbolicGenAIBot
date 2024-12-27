# SymbolicGenAIBot
Symbolic Generative AI Knowledge Bot

Project Overview
This project demonstrates a symbolic AI chatbot designed to provide knowledge about Generative AI concepts, such as LLMs, GANs, Transformers, Datasets, and Applications. The benefits of this project are:
- Excellent foundation for a symbolic AI bot.
- Clean, modular and extensible design.
- Encourages structured learning of Generative AI.

The chatbot uses symbolic reasoning to infer answers from a knowledge base defined in the Entities Relationships dataset, ER.json. It highlights the use of rules and logic in AI reasoning.

Features
- Dynamic reasoning based on entities and relationships from the knowledge base.
- Simple user interface via the command line.
- Fallback responses for unmatched queries.
- Easily extensible knowledge base (in JSON format).

How It Works
1. The knowledge base (ER.json) contains predefined entities, relationships, and details about Generative AI.
2. A custom rule engine that matches user queries to the knowledge base.
3. The bot responds with:
   - Information about entities (e.g., benefits, uses, examples).
   - Fallback responses for unmatched queries.

Usage

Setup
1. Clone the repository: git clone https://github.com/Inder-P-Singh/SymbolicGenAIBot
2. Navigate to the project directory: cd symbolic-generative-ai-bot

Running the Bot
1. Place the ER.json file in the project directory.
2. Run the main script:
    python main.py
3. Enter your query about Generative AI when prompted.

Sample Queries
    "Tell me about GANs."
    "What are the benefits of Transformers?"
    "How are datasets used in Generative AI?"
    "Explain Generative AI applications."

Extending the Knowledge Base
1. Open the ER.json file.
2. Add or modify entities and relationships.
3. Restart the bot to load the updated knowledge base.

Future Enhancements
1. Build a web-based or GUI front-end for user interaction.
2. Add natural language processing for more flexible query handling.
3. Expand the knowledge base with more entities and relationships.

