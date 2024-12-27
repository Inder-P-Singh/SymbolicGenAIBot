# Import Statements
import json
import os
from tabulate import tabulate
print ('Libraries imported')

# Load ER.json
def load_json(file_path):
    """Load JSON file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

class GenerativeAIEngine:
    """
    A custom rule engine to process user queries about Generative AI
    using the knowledge base defined in ER.json.
    """
    def __init__(self, er_data):
        self.er_data = er_data # Load Entities Relationships JSON data
        self.supported_entities = {key.lower(): key for key in er_data["Entities"].keys()}  # Lowercase map
    
    def preprocess_input(self, user_query):
        """
        Preprocess the user query to handle common variations.
        """
        user_query = user_query.strip().lower()
        return user_query

    def find_entity(self, user_query):
        """
        Match the user query to a known entity using normalized input.
        """
        preprocessed_query = self.preprocess_input(user_query)
        for term, original in self.supported_entities.items():
            if term in preprocessed_query:
                return original  # Return the original entity name
        return None

    def handle_query(self):
        """
        Main method to interact with the user and process queries.
        """
        print("Welcome to the Symbolic Generative AI Knowledge Bot!")
        print("Type a query about GenerativeAI (e.g., 'Tell me about LLMs'). No capitalization needed!")
        supported_terms = "GenerativeAI, Datasets, LLMs, Diffusion Models, GANs, Transformers, Applications, Ethics"
        print("Supported terms: ", supported_terms,".\n")

        while True:
            user_query = input("Your query (or type 'exit' to quit): ")
            if user_query.lower() == "exit":
                print("Thank you for using this bot! Goodbye!")
                break

            # Find the matching entity
            entity = self.find_entity(user_query)
            if entity:
                details = self.er_data["Entities"][entity]
                response = f"{entity}: "
                response += " | ".join(
                    f"{relation.capitalize()}: {', '.join(values)}"
                    for relation, values in details.items()
                )
                print(f"\nAI Bot: {response}\n")
            else:
                print("\nAI Bot: I don’t know about that yet. Try asking about: ", supported_terms, "\n")


# Main Execution
if __name__ == "__main__":
    # Load the ER.json file
    folder_path = "/kaggle/input/entitiesrelationships/"
    file_path = folder_path + "ER.json"
    with open(file_path, "r") as f:
        er_data = json.load(f)
    # Create an instance of the custom engine
    ai_engine = GenerativeAIEngine(er_data)
    # Run the query handler
    ai_engine.handle_query()
