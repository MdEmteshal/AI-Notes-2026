from google import genai
from google.genai import types

client=genai.Client(api_key="")

grounding_tool=types.Tool(
    google_search=types.GoogleSearch()
)

response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents="who won the euro cup 2024",
    config=types.GenerateContentConfig(
        tools=[grounding_tool]
    )
)

print(response)