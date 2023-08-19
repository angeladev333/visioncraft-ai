import openai
import os
import dotenv

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_text(idea, budget, items):
    prompt = f"I am looking to build an arduino project based on {idea}. Give me a list of materials I would need to do so. My budget is {budget} and the materials I currently have is {items}."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "user",
            "content": prompt
            }
        ],
        temperature=0.9,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
    )
    content = response.choices[0].message.content
    return content


#generate_text("Ultrasonic object detection module", 1000, ["arduino", "ultrasonic sensor"])