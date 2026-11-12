from dotenv import load_dotenv
from google import genai
import os
import json

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

#summarisation
def summarise_text(text):

    prompt = f"""
    Summarise the following text in 2-3 sentences.

    Preserve the important information.
    Do not add information that is not present.

    Text:
    {text}
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text

# classification
def classify_text(text):

    prompt = f"""
    Classify the following text into one of these categories:

    Positive
    Negative
    Neutral

    Return only the category.

    Text:
    {text}
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text.strip()#reoves unnecessary whitespace from the start and end of the string

# information extraction
def extract_information(text):

    prompt = f"""
    Extract the following information from the text:

    - Name
    - Email
    - College

    Return the result in valid JSON format.

    If any information is missing, use null.
    Do not invent information.

    Text:
    {text}
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )
    result = response.text.strip()

    result = result.replace("```json", "")
    result = result.replace("```", "")

    return json.loads(result)

if __name__ == "__main__": # run this code only if this file is run directly


    sample_text = """
    Aastha is a Computer Science student at BVCOE Delhi.
    She enjoys learning Artificial Intelligence and Backend Development.
    """

    print("\n--- SUMMARISATION ---")
    print(summarise_text(sample_text))

    print("\n--- CLASSIFICATION ---")
    print(classify_text(
        "I absolutely love this product!"
    ))

    print("\n--- INFORMATION EXTRACTION ---")
    print(extract_information(sample_text))