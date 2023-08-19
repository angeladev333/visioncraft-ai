import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

generate_prompt = lambda query: f"{query} in vaporwave style"

def generate_dalle(query):
    response = openai.Image.create(
        prompt=generate_prompt(query),
        n=1,
        size="512x512",
    )
    image_url = response['data'][0]['url']
    return image_url