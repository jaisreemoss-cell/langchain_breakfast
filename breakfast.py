import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# 1. Load the environment variables from the .env file
load_dotenv()

# 2. Initialize the Language Model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# 3. Ask the user for inputs interactively via the terminal
print("Welcome to the Custom Breakfast Generator!")
user_ingredients = input("What ingredients do you have available? (e.g., eggs, spinach, oats): ")

# Keep asking for the number until they enter a valid number <= 5
while True:
    num_ideas_input = input("How many breakfast ideas would you like? (Maximum 5): ")
    if num_ideas_input.isdigit():
        num_ideas = int(num_ideas_input)
        if 1 <= num_ideas <= 5:
            break
        else:
            print("⚠️ Please enter a number between 1 and 5.")
    else:
        print("⚠️ Please enter a valid digit.")

# 4. Construct the prompt for short, concise numbered points without examples
prompt_text = (
    f"I have the following ingredients available: {user_ingredients}. "
    f"Please give me exactly {num_ideas} healthy breakfast ideas using these ingredients. "
    f"Keep them very short and concise as numbered points."
)

message = HumanMessage(content=prompt_text)

# 5. Stream the response live to the terminal
print(f"\n--- {num_ideas} Short Healthy Breakfast Ideas ---")

for chunk in llm.stream([message]):
    print(chunk.content, end="", flush=True)

print() # Adds a clean empty line at the end