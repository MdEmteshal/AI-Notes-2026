from google import genai

client=genai.Client(api_key="")

prompt = input("Enter your prompt: ")

response = client.models.generate_content(
model="gemini-2.5-flash-lite",
contents=prompt
)

print("Generated Content:")
print("--------------xxxxxxxxx--------------")
print(response.text)