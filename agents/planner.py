import json
from llm.llm_client import call_llm

def plan_task(user_task):
    prompt = f"""
You are a Planner Agent.
Convert the task into step-by-step JSON.
Only return valid JSON.

Example format:
{{
  "steps": [
    {{"tool": "github", "query": "python"}},
    {{"tool": "weather", "city": "Delhi"}}
  ]
}}

Task: {user_task}
"""
    plan = call_llm(prompt)
    return json.loads(plan)
 
