from django.db import models
from django.db import models

class News_letter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PredictionHistory(models.Model):
    predicted_class = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.predicted_class

