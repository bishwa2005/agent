from llm.gemini_client import call_gemini

def verify(data: dict) -> str:
    prompt = f"""
You are a Verifier Agent.

Check the data below for completeness and correctness.
Fix missing fields if possible and return a clean structured JSON.

Data:
{data}

Return ONLY valid JSON.
"""
    return call_gemini(prompt)
