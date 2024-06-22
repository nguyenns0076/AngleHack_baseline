import os
import requests
from groq import Groq
import json


with open("config/setting.json", "r") as fin:
    data = json.load(fin)

client = Groq(
    # This is the default and can be omitted
    api_key=data["Groq_API"],
)


def user_create():
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Hi! what can you do?",
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content


def analyze_image_information(image_description, ocr_results):
    prompt = f"""
    Analyze the following image information and provide insights based on the criteria given below:

    Image Description:
    {image_description}

    OCR Results:
    {ocr_results}

    Criteria:
    1. Brand Logos: Identify any brand logos mentioned in the description or OCR results.
    2. Products: Mention any products such as beer kegs and bottles.
    3. Customers: Describe the number of customers, their activities, and emotions.
    4. Promotional Materials: Identify any posters, banners, and billboards.
    5. Setup Context: Determine the scene context (e.g., bar, restaurant, grocery store, or supermarket).

    Insights:
    """
    # Replace with your Groq API key
    data = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}]
    }

    chat_completion = client.chat.completions.create(**data)
    return chat_completion.choices[0].message.content
