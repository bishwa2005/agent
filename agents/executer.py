from tools.github_tool import search_repos
from tools.weather_tool import get_weather

def execute(plan: dict) -> dict:
    results = {}

    for step in plan.get("steps", []):
        tool = step.get("tool")

        if tool == "github":
            results["github"] = search_repos(step["query"])

        elif tool == "weather":
            results["weather"] = get_weather(step["city"])

    return results
