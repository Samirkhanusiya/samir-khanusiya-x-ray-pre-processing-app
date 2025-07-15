import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="X-ray Preprocessing App", layout="centered")

st.title("🩻 X-ray Preprocessing Web App")
st.write("Upload an X-ray image and apply preprocessing: Grayscale, Blur, Histogram Equalization.")

uploaded_file = st.file_uploader("📤 Upload X-ray Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Original Image', use_column_width=True)

    img_np = np.array(image)
    img_cv = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    equalized = cv2.equalizeHist(blur)

    st.subheader("✅ Preprocessed Image")
    st.image(equalized, caption='Grayscale + Blur + Histogram Equalization', use_column_width=True, channels="GRAY")
