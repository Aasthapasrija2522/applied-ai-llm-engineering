# Day 3 – One-shot and Few-shot Prompting

Today I learned about One-shot and Few-shot Prompting and how examples help LLMs understand the expected output.

## What I learned

**1. One-shot Prompting**

In this technique, we provide one example to the model before asking it to perform a task. It helps the model understand the expected format and pattern.

**2. Few-shot Prompting**

Here, we provide multiple examples (2–3 or more) so the model can understand the task by observing different input-output patterns.

**3. Why examples help**

- They make instructions clearer.
- They help the model understand the expected output format.
- They help maintain consistency.
- They demonstrate how similar inputs should be handled.

I also learned about In-Context Learning, where the model uses examples provided in the prompt without retraining.

## Practical Implementation

Implemented Zero-shot, One-shot and Few-shot Prompting using Python and the Gemini API.

- Zero-shot: Classified a customer review without providing examples.
- One-shot: Provided one example before asking for classification.
- Few-shot: Provided three examples (Positive, Negative and Neutral).



## Observation

I compared the responses generated using all three prompting techniques.

The main difference was the number of examples provided in each prompt. I understood how examples guide the model and help it follow a particular output pattern.

## Tasks Completed

- Understood One-shot and Few-shot Prompting.
- Implemented One-shot Prompting using Python.
- Implemented Few-shot Prompting using three examples.
- Compared Zero-shot, One-shot and Few-shot responses.
- Practised using Gemini API.

**Python file:** `day3_prompting.py`

Overall, I learned how providing examples can make LLM prompting more structured and clear.