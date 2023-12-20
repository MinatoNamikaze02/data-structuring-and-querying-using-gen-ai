import os

from flask import Flask, request, jsonify, render_template
from llm import query_gpt4, query_longshot, query_gpt4_non_function
from dotenv import load_dotenv

import utils
import models

app = Flask(__name__)
load_dotenv()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query_llm():
    data: models.Film = utils.fetch_html(os.getenv("url"))
    prompt = request.json['prompt']
    model = request.json['model']
    tokenCount = int(request.json['tokenCount'])
    modelName = request.json['modelName']
    functionCalling = request.json['functionCalling']
    returnNotes = request.json['returnNotes']
   
    prompt =f"""
            Please extract the following information based on the constraints from the given text and return it as a JSON object:

            {prompt}
        """
    data = str([film.dict() for film in data])
    if functionCalling:
        if model == "gpt":
            print("here")
            response = query_gpt4(prompt, tokenCount, modelName, data, returnNotes)
        else:
            response = "Invalid model"

        return jsonify(response)
    else:
        prompt = prompt + "\n" + data
    
    # print(prompt)
    if model == "gpt":
        response = query_gpt4_non_function(prompt, tokenCount, modelName)
    elif model == "mistral":
        response = query_longshot(prompt, tokenCount, modelName)
    else:
        response = "Invalid model"
    
    # print(response)
    return jsonify(response)

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5500)