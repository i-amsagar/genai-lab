import json
import requests
from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()

client = OpenAI()

# --- Tool Definitions ---

def suggest_workout(goal: str):
    print("🔨 Tool Called: suggest_workout", goal)
    workouts = {
        "weight loss": "30-minute HIIT session, 5 days a week",
        "muscle gain": "Push-pull-legs split, 4 days a week with progressive overload",
        "flexibility": "Daily yoga for 20–30 minutes"
    }
    return workouts.get(goal.lower(), "No workout plan found for that goal.")

def calculate_bmi(data: str):
    print("🔨 Tool Called: calculate_bmi", data)
    try:
        info = json.loads(data)
        weight = float(info.get("weight"))
        height = float(info.get("height")) / 100
        bmi = weight / (height ** 2)
        return f"Your BMI is {bmi:.2f}."
    except Exception as e:
        return f"Error calculating BMI: {str(e)}"

def gym_tip(topic: str):
    print("🔨 Tool Called: gym_tip", topic)
    tips = {
        "nutrition": "Focus on high-protein meals and whole foods.",
        "recovery": "Sleep 7–9 hours and stretch regularly.",
        "supplements": "Creatine and whey protein are useful for most lifters."
    }
    return tips.get(topic.lower(), "No tips found for that topic.")

def lookup_info(topic: str):
    print("🔍 Tool Called: lookup_info", topic)
    info_database = {
        "use of creatine": "Creatine is a supplement commonly used to improve strength, increase lean muscle mass, and help muscles recover more quickly during exercise.",
        "benefits of protein": "Protein helps build and repair muscle, supports recovery, and plays a role in hormone production.",
        "what is HIIT": "High-Intensity Interval Training (HIIT) alternates short periods of intense exercise with recovery periods, boosting fat burning and cardiovascular fitness."
    }
    
    result = info_database.get(topic.lower())
    if result:
        return result
    else:
        return f"Sorry, I don't have information about '{topic}'. Try rephrasing or asking about another fitness-related topic."


tools = {
    "suggest_workout": {"fn": suggest_workout, "description": "Suggests workout based on goal."},
    "calculate_bmi": {"fn": calculate_bmi, "description": "Calculates BMI using weight and height."},
    "gym_tip": {"fn": gym_tip, "description": "Gives tips on fitness topics."},
    "lookup_info": {"fn": lookup_info, "description": "Provides general gym or supplement-related information."}
}

# --- Prompt Template ---

system_prompt = f"""
    You are an helpful Gym Assistant AI who is specialized in resolving user query.
    You work on start, plan, action, observe mode.
    For the given user query and available tools, plan the step by step execution, based on the planning, select the relevant tool from the available tool. and based on the tool selection you perform an action to call the tool.
    Wait for the observation and based on the observation from the tool call resolve the user query.

    Output JSON Format:
    {{
        "step": "plan" | "action" | "observe" | "output",
        "content": "string",
        "function": "The name of function if the step is action",
        "input": "The input parameter for the function",
    }}

    Rules:
    - Follow the Output JSON Format.
    - Always perform one step at a time and wait for next input
    - Carefully analyse the user query

    Available Tools:
    - suggest_workout: Input is goal like "muscle gain"
    - calculate_bmi: Input is JSON string with weight and height
    - gym_tip: Input is a topic like "nutrition", "recovery", or "supplements"
    - lookup_info: Provides general gym or supplement-related information"

    Example:
    User Query: What is the use of creatine?
    Output: {{ "step": "plan", "content": "The user is asking about the purpose or benefits of creatine" }}
    Output: {{ "step": "plan", "content": "This is a general knowledge query, so I should retrieve or explain information from known sources" }}
    Output: {{ "step": "action", "function": "lookup_info", "input": "use of creatine" }}
    Output: {{ "step": "observe", "output": "Creatine is a supplement commonly used to improve strength, increase lean muscle mass, and help muscles recover more quickly during exercise." }}
    Output: {{ "step": "output", "content": "Creatine is typically used to improve strength, build muscle mass, and aid muscle recovery during high-intensity exercise." }}
"""

# --- Run Agent Loop ---

messages = [{"role": "system", "content": system_prompt}]

while True:
    print("Enter you query:")
    user_query = input("> ")
    messages.append({"role": "user", "content": user_query})

    while True:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            response_format={"type": "json_object"},
        )

        parsed = json.loads(response.choices[0].message.content)
        messages.append({"role": "assistant", "content": json.dumps(parsed)})

        step = parsed.get("step")

        if step == "plan":
            print(f"🧠: {parsed['content']}")
            continue

        elif step == "action":
            tool_name = parsed["function"]
            tool_input = parsed["input"]
            tool = tools.get(tool_name)
            if tool:
                output = tool["fn"](tool_input)
                messages.append({
                    "role": "assistant",
                    "content": json.dumps({"step": "observe", "output": output})
                })
                continue

        elif step == "output":
            print(f"🤖: {parsed['content']}")
            break
