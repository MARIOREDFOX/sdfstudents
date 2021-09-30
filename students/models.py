from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=12)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name.upper()