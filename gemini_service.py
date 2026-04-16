import json
import re
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found.")

client = genai.Client(api_key=API_KEY)

def generate_micro_modules(raw_text: str, domains: list) -> list:
    domain_str = ", ".join(domains)
    prompt = f"""You are creating training content for a financial services company.
Selected domains: [{domain_str}].
Break the text into 2-minute learning sprints.
Return ONLY a valid JSON array, no markdown, no explanation.
Format: [{{"title": "...", "content": "...", "reading_time_minutes": 2}}]
Text: \"\"\"{raw_text}\"\"\""""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    raw = re.sub(r"```json|```", "", response.text.strip()).strip()
    try:
        return json.loads(raw)
    except:
        return [{"title": "Module 1", "content": raw, "reading_time_minutes": 2}]