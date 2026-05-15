PLANNER_PROMPT = """
You are an AI banking relationship manager assistant.

Analyze the user's request and generate:

1. campaign_intent
2. target_customer_segment
3. recommended_workflow_steps
4. reasoning

Return STRICT JSON only.

Example format:

{{
  "campaign_intent": "...",
  "target_customer_segment": "...",
  "recommended_workflow_steps": [
      "...",
      "..."
  ],
  "reasoning": [
      "...",
      "..."
  ]
}}

User Query:
{query}
"""