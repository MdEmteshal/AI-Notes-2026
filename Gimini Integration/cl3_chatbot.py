from google import genai
from google.genai import types

client=genai.Client(api_key="")

print("Welcome to the Gemini Chatbot!")
print("You can ask questions or type 'exit' to quit.")

chat=[]

userinput = input("User: ")
while userinput != "exit":
    chat.append(("user :" + userinput))

    systemoutput = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=chat,
        config=types.GenerateContentConfig( 
            system_instruction="Answer in 1 line ,within 50 characters"
        )
    )
     
    chat.append(("startbot :" + systemoutput.text))
    print("startbot:",systemoutput.text)
    print("--------------xxxxxxxxx--------------")
    userinput = input("User: ")