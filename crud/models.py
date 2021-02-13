from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.TextField()
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name