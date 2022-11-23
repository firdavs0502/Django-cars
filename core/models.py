from django.db import models

# Create your models here.





class Post1(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    time = models.TimeField(auto_now_add=True)
    rasmcha = models.CharField(max_length=200)

    def __str__(self):
        return self.name
