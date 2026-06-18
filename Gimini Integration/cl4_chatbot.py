from google import genai
from google.genai import types

client=genai.Client(api_key="")

chat = client.chats.create(
    model="gemini-2.5-flash-lite",      
)

print("Welcome to the Gemini Chatbot!")
print("You can ask questions or type 'exit' to quit.")

userinput = input("User: ")
while userinput != "exit":
    
    response = chat.send_message(
        content=userinput                  ) 
    # print("startbot:" + response.text)
    print("--------------xxxxxxxxx--------------")
    userinput = input("User: ")

for message in chat.get_history():
    print(f"role-{message.role}")
    print(message.parts[0].text)