import openai
import os
import re

openai.api_key = "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"

def generate_text(idea, budget, items):
    prompts = [f"i am writing a diy tutorial for building an {idea} station using Arduino. provide an introduction to the tutorial (around 600 words)", f"i am writing a diy tutorial for building an {idea} using Arduino. i currently have the following items {items} - you must use them in the materials list. my budget is {budget}. provide a list of materials for the tutorial (around 600 words). include some fluff text before these materials that does not mention an introduction", f"i am writing a diy tutorial for building an {idea} using Arduino. provide a procedure for the tutorial (around 600 words). include some fluff text before this procedure that does not mention an introduction", f"i am writing a diy tutorial for building an {idea} using Arduino. provide a list of important considerations when building to be added to the tutorial (around 600 words). include some fluff text before these considerations that does not mention an introduction"]
    contents = []
    for prompt in prompts:
        print(f"Currently computing: {prompt}")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                "role": "user",
                "content": prompt
                }
            ],
            temperature=0,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
        )
        content = response.choices[0].message.content
        paragraphs = content.split('\n\n')
        remaining_text = '\n\n'.join(paragraphs[1:])
        contents.append(remaining_text)
    print(contents)
    return contents



