import os
import random

import openai
import requests
import together
from dotenv import load_dotenv

import custom_functions

load_dotenv()

# Function to interact with OpenAI's GPT-4
def query_gpt4(prompt, tokenCount, model_name, data, returnNotes):
    openai.api_key = os.getenv("OPEN_AI_KEY")
    random_temperature = random.uniform(0, 1)
    try:
        if returnNotes:
            custom_function = custom_functions.custom_function_all(prompt)
            function = "extract_film_info_based_on_prompt"
        else:
            custom_function = custom_functions.custom_function(prompt)
            function = "extract_all_film_info_based_on_prompt"
        response = openai.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "user", "content": prompt},
                {"role": "function", "name": function, "content": data},
            ],
            functions=custom_function,
            function_call="auto",
            max_tokens=tokenCount,
            temperature=random_temperature,
            
        )
        return response.choices[0].message.function_call.arguments

    except Exception as e:
        return "Error" + str(e)
    
def query_gpt4_non_function(prompt, tokenCount, model_name, data):
    openai.api_key = os.getenv("OPEN_AI_KEY")
    random_temperature = random.uniform(0, 1)
    try:
        response = openai.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": data}
            ],
            max_tokens=tokenCount,
            temperature=random_temperature,
        )
        return response.choices[0].message.content
    except Exception as e:
        return "Error" + str(e)

# Function to interact with Mistral LLM
def query_longshot(prompt, tokenCount, model_name):
    together.api_key = os.getenv("TOGETHER_AI_KEY")
    try:
        output = together.Complete.create(
            prompt=prompt,
            model = model_name,
            max_tokens=tokenCount,
            temperature=0.7,
        )
        return output['output']['choices'][0]['text']
    except Exception as e:
        return "Error" + str(e)
