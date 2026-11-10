
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Input text
text = """
Artificial Intelligence is transforming various industries.
It is used in healthcare, education, finance, and transportation.
AI helps automate repetitive tasks, analyze large amounts
of data, and improve decision-making.
"""

# Zero-shot prompt
prompt = f"""
Summarize the following paragraph in 3-4 sentences
using simple English.

{text}
"""

# Generate response
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

# Display output
print("Original Text:")
print(text)

print("\nGenerated Summary:")
print(response.text)
