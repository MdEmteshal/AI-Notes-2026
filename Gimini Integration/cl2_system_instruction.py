from google import genai
from google.genai import types
from PIL import Image

client=genai.Client(api_key="")

image=Image.open("images/portfolio.png")

# prompt = input("Enter your prompt: ")

response = client.models.generate_content(
model="gemini-2.5-flash-lite",
contents=[image,"Tell me about this image"],
config=types.GenerateContentConfig( 
    system_instruction="response should be 30 words",
    temperature=0.1
)
)

print("Generated Content:")
print("--------------xxxxxxxxx--------------")
print(response.text)