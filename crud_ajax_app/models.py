from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=255)
    address=models.TextField()
    phone_number=models.CharField(max_length=11)
    slug=models.SlugField(null=True,blank=True)
    

    def __str__(self):
        return self.name