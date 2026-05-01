import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from PIL import Image

model = load_model("mask_detector.h5")

st.title("😷 Face Mask Detection App")

uploaded_file = st.file_uploader("Upload Image", type=["jpg","png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

    img = np.array(image)
    img = cv2.resize(img,(128,128))
    img = img/255.0
    img = np.reshape(img,(1,128,128,3))

    pred = model.predict(img)

    if pred < 0.5:
        st.success("Mask Detected 😷")
    else:
        st.error("No Mask Detected ❌")