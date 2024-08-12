import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from PIL import Image

# Model loading
MODEL_FILENAME = 'mi_modelo.h5'
MODEL_PATHS = [
    MODEL_FILENAME,  # Try to load from the current directory first
    os.path.join('src', MODEL_FILENAME),  # Then try the 'src' subdirectory
    os.path.join(os.path.dirname(__file__), MODEL_FILENAME),  # Then try the script's directory
    os.path.join(os.path.dirname(__file__), 'src', MODEL_FILENAME)  # Finally, try 'src' in the script's directory
]

@st.cache_resource
def load_model_cached():
    for path in MODEL_PATHS:
        if os.path.exists(path):
            return load_model(path)
    raise FileNotFoundError(f"Model file '{MODEL_FILENAME}' not found in any of the expected locations.")

try:
    model = load_model_cached()
    st.success("Model loaded successfully!")
except FileNotFoundError as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Sample images directory
SAMPLE_IMG_DIR = 'image_sample'

# Banner image path
BANNER_FILENAME = 'banner.jpeg'
BANNER_PATHS = [
    os.path.join('assets', BANNER_FILENAME),
    os.path.join(os.path.dirname(__file__), 'assets', BANNER_FILENAME)
]

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
banner_displayed = False
for path in BANNER_PATHS:
    if os.path.exists(path):
        st.image(path, use_column_width=True)
        banner_displayed = True
        break
if not banner_displayed:
    st.warning("Banner image not found. Please check the path.")

st.title('Malaria Detector')

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

# Configuration information and instructions
st.sidebar.title("Configuration Information")
st.sidebar.info(f"""
Current configuration:
- Model: The model file should be named '{MODEL_FILENAME}' and be in the main directory or in a 'src' subdirectory.
- Sample images folder: {SAMPLE_IMG_DIR}
- Banner image: The banner should be named '{BANNER_FILENAME}' and be in an 'assets' folder.

Please ensure that:
1. The model file ({MODEL_FILENAME}) is in the correct location.
2. The sample images folder contains the images you want to use for testing.
3. The images are in jpg, png, or jpeg format.
4. The banner image is in the assets folder.
""")