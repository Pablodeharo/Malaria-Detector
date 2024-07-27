from django.db import models

class Prediction(models.Model):
    image = models.ImageField(upload_to='uploads/')
    result = models.CharField(max_length=50)
    confidence = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
