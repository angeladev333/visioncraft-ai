import openai
import os
import requests
import shutil
from random import randint

openai.api_key = "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" 

generate_prompt = lambda query: f"A photorealistic photo of {query}. High Resolution 4k Nikon Camera 24.2MP"

def generate_dalle(query):
    response = openai.Image.create(
        prompt=generate_prompt(query),
        n=5,
        size="256x256",
    )
    file_names=[]
    for i in range(0, len(response['data'])):
        image_url = response['data'][i]['url']
        image_res = requests.get(image_url, stream=True)
        file_name = f"server/tmp/{randint(0, 1000000)}.png"
        file_names.append(file_name)
        with open(file_name, "wb") as out_file:
            shutil.copyfileobj(image_res.raw, out_file)
        del image_res
        
    return file_names 