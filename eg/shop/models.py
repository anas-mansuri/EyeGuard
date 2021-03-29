from django.db import models

# Create your models here.
class contacts(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=13)
    message=models.CharField(max_length=300)

    def __str__(self):
        return self.name