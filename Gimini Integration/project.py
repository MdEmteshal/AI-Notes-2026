from google import genai
from google.genai import types
from pydantic import BaseModel
from typing import Optional
import json


class planSteps(BaseModel):
     step_name:str

class ExecuteTask(BaseModel):
     task_name:str
     action_performed:str
     summary:str
     simulated_data: Optional[str]=None

def callmodel(prompt,schema):
     response = chat.send_message(prompt,config=types.GenerateContentConfig(
          response_schema=schema,
          response_mime_type="application/json",
          system_instruction="Answer within 30 words"
     ))
     return response.text

def plan_goal():
     
     plan_prompt="Break the goal into clear, numbered steps"
     plans=callmodel(plan_prompt,list[planSteps])
     plans=json.loads(plans)
     steps=[plan["step_name"].strip() for plan in plans if plan['step_name'].strip()]
     return steps

def execute_step(step):
     print("<---------------->")
     action_prompt=f"Execute this task : {step}. Describe what you did and summarize the result . Simulate the task if required"
     result=callmodel(action_prompt,ExecuteTask)

     result=json.loads(result)

     print("Task : ", result['task_name'])
     print("Action :", result['action_performed'])
     print("Summary :",result['summary'])

     if result['simulated_data']:
          print("Data :",result['Simulated_data'].strip())
     print("<---------------->")




def run_agent():
    steps=plan_goal()
   
    for step in steps:
        print(step)
        # execute_step(step)

    print("\n completed steps \n")

if __name__ == "__main__":
        client=genai.Client(api_key="")
        model="gemini-2.5-flash-lite"
        chat=client.chats.create(model=model)
        goal="Book a ticket from londom to New York"
        print(f"Goal: {goal}")
        modified_goal=f""" you are a virtual agent expert in booking tickets. Your goal is {goal}.for Know acknowledge the goal, goaing forward I will be asking you to creat a plan and execute the plans"""


        chat.send_message(modified_goal)

#run -> plan steps -> execute steps