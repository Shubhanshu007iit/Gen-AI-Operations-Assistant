from llm.llm_client import call_llm
import json

def verify_and_format(data):
    prompt = f"""
You are a Verifier Agent.
Check completeness and format a clean response.

Data:
{json.dumps(data, indent=2)}
"""
    return call_llm(prompt)
