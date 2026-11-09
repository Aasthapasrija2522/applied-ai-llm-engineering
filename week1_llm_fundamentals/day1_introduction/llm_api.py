
import os

from dotenv import load_dotenv
from google import genai

# Step 1: Load environment variables
load_dotenv()

# Step 2: Get API key and model name
api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL", "gemini-flash-latest")

# Step 3: Check API key
if not api_key:
    raise ValueError("Gemini API key not found!")

# Step 4: Create Gemini client
client = genai.Client(api_key=api_key)

# Step 5: Take input from user
prompt = input("Enter your question: ")

# Step 6: Send prompt to Gemini
response = client.interactions.create(
    model=model,
    input=prompt
)

# Step 7: Print the response
print("\nGemini Response:")
print(response.output_text)

# Step 8: Close client
client.close()
