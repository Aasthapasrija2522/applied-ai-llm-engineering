
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# One-shot prompting: providing one example
prompt = """
Classify customer reviews as Positive, Negative, or Neutral.

Example:
Review: The product is amazing and I love it.
Sentiment: Positive

Now classify this review:

Review: The product quality is excellent, but delivery was very slow.
Sentiment:
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt #ai ko input kya dena h 
)

print("ONE-SHOT PROMPTING")
print("Response:", response.text) # gemini ka ans print krna 



# Few-shot prompting: providing three examples

few_shot_prompt = """
Classify customer reviews as Positive, Negative, or Neutral.

Example 1:
Review: The product is amazing and I love it.
Sentiment: Positive

Example 2:
Review: The product is damaged and the quality is terrible.
Sentiment: Negative

Example 3:
Review: The product is okay, nothing special.
Sentiment: Neutral

Now classify this review:

Review: The product quality is excellent, but delivery was very slow.
Sentiment:
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=few_shot_prompt
)

print("\\nFEW-SHOT PROMPTING")
print("Response:", response.text)
