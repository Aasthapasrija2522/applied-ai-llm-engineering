Day 1 – Introduction to Large Language Models (LLMs)

1. What is Artificial Intelligence (AI)?

AI ka simple meaning hai machines ko aise tasks karne ke capable banana jinke liye normally human intelligence ki zarurat hoti hai.

Examples:

Voice assistants

Face recognition

Chatbots

Recommendation systems

2. What is Machine Learning (ML)?

ML, AI ka ek part hai jisme machines data se patterns learn karti hain aur uske basis par predictions ya decisions leti hain.

Example: Gmail ka spam filter purane emails se learn karke identify karta hai ki kaunsa email spam ho sakta hai.

3. What is Generative AI?

Generative AI aisi AI hai jo existing data se patterns learn karke new content generate kar sakti hai.

It can generate:

Text

Images

Audio

Videos

Code

Examples: ChatGPT, Google Gemini and image-generation models.

4. What is a Large Language Model (LLM)?

LLM ek AI model hai jise bahut saare text data par train kiya jata hai, taaki woh human language ko understand karke responses generate kar sake.

LLMs can be used for:

Answering questions

Summarising content

Writing emails or articles

Generating code

Translating languages

Examples: GPT, Gemini, Claude and Llama.

5. Traditional ML vs LLMs

Traditional ML

LLMs

Mostly specific tasks ke liye use hota hai.

Multiple language-related tasks kar sakte hain.

Data ke patterns se predictions karta hai.

Language ko process karke responses generate karta hai.

Classification aur prediction mein commonly used hai.

Text generation, summarisation aur coding mein useful hai.

Usually task-specific training ki zarurat hoti hai.

Prompts ke through different instructions follow kar sakte hain.

6. How Does an LLM Generate a Response?

Jab hum LLM ko koi question dete hain, toh roughly ye process follow hota hai:

Input: Hum model ko ek prompt dete hain.

Tokenization: Prompt small parts mein break hota hai, jinhe tokens kehte hain.

Prediction: Model given context ke basis par next likely token predict karta hai.

Generation: Model ek-ek token generate karke complete response banata hai.

My Understanding: LLM simply ready-made answers search nahi karta. Ye training ke time learned patterns aur current context ke basis par response generate karta hai.

7. What is an API?

API ka full form Application Programming Interface hai.

Simple words mein, API ek medium hai jiske through two applications aapas mein communicate kar sakti hain.

Example: Hum Python se Gemini API ko request bhej sakte hain aur Gemini se response receive kar sakte hain.

Basic API Flow

Client API ko request send karta hai.

API request ko process karti hai.

Server required task perform karta hai.

Response wapas client ko mil jata hai.

8. What is an LLM API Call?

LLM API call ka matlab hai apne code ke through kisi language model se interact karna.

Day 1 practical mein maine:

Python se Gemini API connect karne ki koshish ki.

API key ko .env file mein store kiya.

google-genai SDK use kiya.

Gemini ko text prompt send karne ka code likha.

Model se generated response receive karne ka process samjha.

9. Key Learnings

AI is the broader field and ML is a part of AI.

Generative AI new content create kar sakti hai.

LLMs human language ko process aur generate karne ke liye trained hote hain.

Prompt humari instruction hoti hai jo model ko batati hai ki kya karna hai.

Tokens text ke small units hote hain.

API ki help se hum LLMs ko apne Python applications mein use kar sakte hain.