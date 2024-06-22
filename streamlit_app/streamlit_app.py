import streamlit as st
from PIL import Image
from text_extractor.extract_text_easyocr import perform_ocr
from image_caption.img_cap import get_image_caption
from combine_by_llm.llm_combine import analyze_image_information


def streamlit_app():
    # Streamlit app
    st.set_page_config(layout="wide")
    st.title("Image Analysis App")

    # Create three columns with custom widths
    col1, col2, col3 = st.columns([1, 2, 2])

    with col1:
        st.header("Upload Image")
        uploaded_file = st.file_uploader(
            "Choose an image file", type=["jpg", "jpeg", "png"])

    with col2:
        st.header("OCR and Description")

        if uploaded_file is not None:
            # Load the image
            image = Image.open(uploaded_file).convert("RGB")
            st.image(image, caption='Uploaded Image', use_column_width=True)

            # Get image caption
            st.subheader("Image Description")
            image_description = get_image_caption(image)
            st.write(image_description)

            # # Perform OCR
            # st.subheader("OCR Texts")
            ocr_texts = perform_ocr(image)
            # for text in ocr_texts:
            #     st.write(text)

    with col3:
        st.header("Analysis")

        if uploaded_file is not None:
            # Analyze image information
            ocr_results = ' '.join(ocr_texts)
            analysis = analyze_image_information(
                image_description, ocr_results)
            st.write(analysis)
