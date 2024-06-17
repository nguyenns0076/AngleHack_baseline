import easyocr
import cv2
import numpy as np
from matplotlib import pyplot as plt


def ocr_image(image_path):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(image_path)
    return result


def extract_imformation(img_path=""):

    mat = cv2.imread(img_path)
    result = ocr_image(img_path)

    boxes = [line[0] for line in result]
    texts = [line[1] for line in result]
    # scores = [line[2] for line in result]

    for box, text in zip(boxes, texts):
        top_left = (int(box[0][0]), int(box[0][1]))
        bottom_right = (int(box[2][0]), int(box[2][1]))

        cv2.rectangle(mat, top_left, bottom_right, (0, 255, 0), 2)
        cv2.putText(mat, text, top_left,
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    mat = cv2.cvtColor(mat, cv2.COLOR_BGR2RGB)

    plt.imshow(mat)
    return texts


# Initialize the OCR reader
ocr_reader = easyocr.Reader(["en"])


def perform_ocr(image):
    result = ocr_reader.readtext(np.array(image))
    ocr_texts = [line[1] for line in result]
    return ocr_texts
