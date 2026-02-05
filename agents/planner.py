import json
from llm.gemini_client import call_gemini

def plan(task: str) -> dict:
    prompt = f"""
You are a Planner Agent.

Available tools:
1. github → needs: query
2. weather → needs: city

Convert the user task into a step-by-step JSON plan.

User task:
{task}

Output ONLY valid JSON in this format:
{{
  "steps": [
    {{ "tool": "github", "query": "example" }},
    {{ "tool": "weather", "city": "example" }}
  ]
}}
"""
    response = call_gemini(prompt)
    return json.loads(response)
