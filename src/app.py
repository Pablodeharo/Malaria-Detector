import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Ruta completa al archivo del modelo
model_path = r'C:\Users\lenovo\Desktop\Malaria Detection\Malaria Detector\src\mi_modelo.h5'
model = load_model(model_path)

st.title('Clasificación de Imágenes de Malaria')

uploaded_file = st.file_uploader("Elige una imagen...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagen subida.', use_column_width=True)
    st.write("")
    st.write("Clasificando...")

    # Preprocesar la imagen
    image = image.resize((224, 224))
    image = np.array(image)
    image = image.reshape((1, 224, 224, 3))

    # Realizar la predicción
    prediction = model.predict(image)
    class_idx = np.argmax(prediction, axis=1)

    st.write(f'La imagen es de la clase: {class_idx[0]}')
