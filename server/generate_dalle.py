import openai
import os
import requests
import shutil
from random import randint

openai.api_key = os.getenv("OPENAI_API_KEY")

generate_prompt = lambda query: f"{query} in vaporwave style"

def generate_dalle(query):
    response = openai.Image.create(
        prompt=generate_prompt(query),
        n=4,
        size="256x256",
    )
    file_names=[]
    for i in range(0, len(response['data'])):
        image_url = response['data'][i]['url']
        image_res = requests.get(image_url, stream=True)
        file_name = f"tmp/{randint(0, 1000000)}.png"
        file_names.append(file_name)
        with open(file_name, "wb") as out_file:
            shutil.copyfileobj(image_res.raw, out_file)
        del image_res
        
    return file_names   
