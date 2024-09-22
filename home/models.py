from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=15)  
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):  # Corrected the method name
        return self.name
