# importing requried modules
import openai
import time
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
from dotenv import load_dotenv

# load all the env variables    
load_dotenv()
app = Flask(__name__)
CORS(app)


openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_type = "azure"
openai.api_version = "2023-05-15"
api_version_img = "2023-06-01-preview"
    
model_name:str = "Azure-OpenAI-Demo"

messages  = [ {
        "role":"user",
        "content": "Hi there!"
    }
]

def get_response():
    try:
        response = openai.ChatCompletion.create(
                   engine=model_name,
        messages=messages,
        max_tokens=1000,
        temperature=1,
        )
        return response
    except Exception as exp:
        print("Exception occurs",exp)



def cook_model_msg(model_response):
    model_msg = {
        "role":model_response.choices[0].message.role,
        "content": model_response.choices[0].message.content
    }
    return model_msg


@app.route('/process_request',methods=['POST'])
def process_request():
    user_prompt = request.get_json()['message']
    msg = {
    "role":"user",
    "content":  f'{user_prompt}'
    }
    messages.append(msg)
    model_response = get_response()
    model_message = cook_model_msg(model_response=model_response)
    messages.append(model_message)
    return jsonify(model_message)


@app.route('/generate_image',methods=['POST'])
def generate_image():
    user_query_text = request.get_json()['content']
    try:
        url = "{}openai/images/generations:submit?api-version={}".format(openai.api_base,api_version_img)
        headers = {"api-key": openai.api_key, "Content-Type":"application/json"}
        body = {
            "prompt":str(user_query_text),
            "n":1,
            "size":"512x512"
        }
        submission = requests.post(
            url,headers=headers,json=body
        )

        operation_location = submission.headers['Operation-Location']
        status = ""
        while (status != "succeeded"):
            time.sleep(3)
            response = requests.get(operation_location, headers=headers)
            status = response.json()['status']

        image_url = response.json()['result']['data'][0]['url']
        res = {
            "role":"assistant",
            "url":image_url
        }
        return jsonify(res)
    except Exception as exp:
        print("Exception occurs",exp)


if __name__ == "__main__":
    app.run(debug=True)