
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Common user prompt
user_prompt = "Explain what an API is."

# Different system instructions
roles = {
    "TEACHER": """
    You are an experienced computer science teacher.
    Explain concepts in simple language.
    Use real-world examples.
    Assume the user is a beginner.
    """,

    "SOFTWARE ENGINEER": """
    You are a senior software engineer.
    Explain technical concepts with practical details.
    Discuss architecture, implementation and use cases.
    """,

    "INTERVIEWER": """
    You are a technical interviewer.
    Explain concepts in an interview-oriented manner.
    Focus on definitions, key points and follow-up questions.
    """
}

# Run all roles
for role, instruction in roles.items():
    print("--------------------")
    print(role)
    print("--------------------")

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=user_prompt,
        config={
            "system_instruction": instruction
        }
    )

    print(response.text)
