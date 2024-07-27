from django.shortcuts import render

from django.shortcuts import render
from .forms import ImageUploadForm
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

def predict_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data['image']
            img_array = image.img_to_array(image.load_img(img, target_size=(224, 224)))
            img_array = np.expand_dims(img_array, axis=0) / 255.0

            model_path = r'C:/Users/lenovo/Desktop/Malaria Detection/Malaria Detector/src/mi_modelo.h5'
            model = load_model(model_path)
            
            prediction = model.predict(img_array)
            result = 'Infected' if prediction[0][0] > 0.5 else 'Uninfected'
            confidence = prediction[0][0] if result == 'Infected' else 1 - prediction[0][0]

            return render(request, 'result.html', {'result': result, 'confidence': confidence})
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})
