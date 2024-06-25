import os
import cohere
from langchain_community.llms import Cohere

# Set the Cohere API key as an environment variable
os.environ['COHERE_API_KEY'] = "RoW3TACuTTMx8B7vBrFTnByB3YyMT5MJmbRpXscP"

# Initialize the Cohere LLM with the API key
cohere_client = cohere.Client(os.getenv('COHERE_API_KEY'))
llm = Cohere(client=cohere_client)

# Use the LLM to generate a response
response = llm("List the seven wonders of the world.")
print(response)