from text_extractor.extract_text_easyocr import extract_imformation
from image_caption.img_cap import img_cap
from combine_by_llm.llm_combine import analyze_image_information
from streamlit_app.streamlit_app import streamlit_app

# img_path = "data/Heineken Vietnam/66506043_1708621535998.jpg"
# texts = extract_imformation(img_path)
# description = img_cap(img_path)

# image_description = description[0]['generated_text']
# ocr_results = ' '.join(texts)

# analysis = analyze_image_information(image_description, ocr_results)
# print(analysis)

streamlit_app()
