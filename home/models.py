from django.db import models

# Create your models here.
class Contact(models.Model):
    sno= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone= models.CharField(max_length=13)
    message = models.TextField()
    timestamp= models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name