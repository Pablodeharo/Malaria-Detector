import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from PIL import Image

# Load the model
MODEL_PATH = r'C:\Users\lenovo\Desktop\Malaria Detection\Malaria Detector\src\mi_modelo.h5'
model = load_model(MODEL_PATH)

# Sample images directory
SAMPLE_IMG_DIR = r'C:\Users\lenovo\Desktop\Malaria Detection\Malaria Detector\src\image_sample'

# Banner image path
BANNER_PATH = r'C:\Users\lenovo\Desktop\Malaria Detection\Malaria Detector\src\assets\banner.jpeg'

def preprocess_image(img):
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return img / 255.0

def predict(img):
    preprocessed_img = preprocess_image(img)
    prediction = model.predict(preprocessed_img)
    return prediction[0][0]

def resize_image(img, max_size=(300, 300)):
    img.thumbnail(max_size)
    return img

# Display banner
st.image(BANNER_PATH, use_column_width=True)

# Create three columns for the buttons
col1, col2, col3 = st.columns(3)

# GitHub button
with col1:
    github_html = """
    <a href="https://github.com/Pablodeharo/Phishing-Domain-Detection" target="_blank">
        <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="30" height="30">
        GitHub
    </a>
    """
    st.markdown(github_html, unsafe_allow_html=True)

# LinkedIn button
with col2:
    linkedin_html = """
    <a href="https://www.linkedin.com/in/pablo-de-haro-pishoudt-0871972b6/" target="_blank">
        <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="30" height="30">
        LinkedIn
    </a>
    """
    st.markdown(linkedin_html, unsafe_allow_html=True)

# Documentation (Notion) button
with col3:
    notion_html = """
    <a href="https://tiny-citrine-a6e.notion.site/Phishing-Domain-Detection-a9c3c58fc27746b586d43352e4ebe075" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/4/45/Notion_app_logo.png" width="30" height="30">
        Documentation
    </a>
    """
    st.markdown(notion_html, unsafe_allow_html=True)

st.title('Malaria Detector')

# Option to choose between uploading image or using sample
option = st.radio(
    "Choose an option:",
    ('Upload my own image', 'Use a sample image')
)

if option == 'Upload my own image':
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        img_display = resize_image(img.copy())
        img = img.resize((224, 224))
        st.image(img_display, caption='Uploaded Image', use_column_width=False)
else:
    # List of sample images
    sample_images = os.listdir(SAMPLE_IMG_DIR)
    selected_sample = st.selectbox("Choose a sample image:", sample_images)
    img_path = os.path.join(SAMPLE_IMG_DIR, selected_sample)
    img = Image.open(img_path)
    img_display = resize_image(img.copy())
    img = img.resize((224, 224))
    st.image(img_display, caption='Selected Sample Image', use_column_width=False)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button('Predict'):
        prediction = predict(img)
        if prediction > 0.5:
            st.error(f'Prediction: Infected with malaria (Probability: {prediction:.2f})')
        else:
            st.success(f'Prediction: Not infected (Probability: {1-prediction:.2f})')

