from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class folder(models.Model):
    language = models.CharField(max_length=100)
    upload = models.FileField(upload_to='Desktop/')

    def __str__(self):
        return self.language
