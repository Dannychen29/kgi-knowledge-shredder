import google.generativeai as genai
import json
import re
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Please create a .env file with your API key.")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("models/gemini-2.5-flash")

def generate_micro_modules(raw_text: str, domains: list[str]) -> list[dict]:
    domain_str = ", ".join(domains)

    prompt = f"""
You are creating training content for a financial services company.
The selected knowledge domains are: [{domain_str}].

Your task:
- Read the text below carefully.
- Break it into 2-minute learning sprints (micro-modules).
- Each module should be self-contained and focused.
- Tone should be professional, clear, and engaging.
- Emphasize concepts relevant to the domains: {domain_str}.

Return ONLY a valid JSON array. No explanation, no markdown, no extra text.
Format:
[
  {{
    "title": "Short title of this module",
    "content": "The full learning content for this 2-minute sprint.",
    "reading_time_minutes": 2
  }},
  ...
]

Text to process:
\"\"\"
{raw_text}
\"\"\"
"""

    response = model.generate_content(prompt)
    raw_response = response.text.strip()

    # Clean markdown code fences if present
    raw_response = re.sub(r"```json|```", "", raw_response).strip()

    try:
        modules = json.loads(raw_response)
        return modules
    except json.JSONDecodeError:
        # Fallback: return single module with raw content
        return [{
            "title": "Module 1",
            "content": raw_response,
            "reading_time_minutes": 2
        }]