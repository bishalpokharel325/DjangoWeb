from django.db import models
from ckeditor.fields import RichTextField
class Slider(models.Model):
    title=models.CharField(max_length=150,unique=True)
    description=RichTextField()
    image=models.ImageField(upload_to="Slider")
    status=models.BooleanField(default=0)
    created_at=models.DateField()
    slug=models.CharField(max_length=150,unique=True)
def __str__(self):
    return self.title




# Create your models here.
