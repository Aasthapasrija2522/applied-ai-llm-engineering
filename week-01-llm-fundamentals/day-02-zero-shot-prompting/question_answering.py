
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Input question
question = "What is Machine Learning?"

# Zero-shot prompt
prompt = f"""
Answer the following question in simple English.

Provide:
1. A clear definition.
2. Three important points.
3. One real-world example.

Question: {question}
"""

# Generate response
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

# Display output
print("Question:")
print(question)

print("\nGenerated Answer:")
print(response.text)
