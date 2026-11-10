from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

review = "The product is excellent and delivery was fast."

prompt = f"""
Classify this review as Positive, Negative, or Neutral.
Give one-line reason.

Review: {review}
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

print(response.text)