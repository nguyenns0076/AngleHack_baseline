import cv2
from transformers import pipeline
from PIL import Image
import numpy as np
import json

with open("config/setting.json", "r") as fin:
    data = json.load(fin)


def img_cap(img_path=""):
    # Initialize the image captioning pipeline
    pipe = pipeline("image-to-text",
                    model="Salesforce/blip-image-captioning-base")

    img = Image.open(img_path).convert("RGB")

    # Generate a description for the image
    description = pipe(img)
    return description


def get_image_caption(image):
    # Use a pre-trained image captioning model from Salesforce
    caption_pipeline = pipeline(
        "image-to-text", model="Salesforce/blip-image-captioning-base")
    return caption_pipeline(image)[0]['generated_text']
