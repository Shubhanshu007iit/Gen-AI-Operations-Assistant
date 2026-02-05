from tools.github_tool import search_github
from tools.weather_tool import get_weather

def execute_plan(plan):
    results = {}

    for step in plan["steps"]:
        if step["tool"] == "github":
            results["github"] = search_github(step["query"])

        if step["tool"] == "weather":
            results["weather"] = get_weather(step["city"])

    return results
