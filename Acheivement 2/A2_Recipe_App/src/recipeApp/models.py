from django.db import models


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=255)
    cooking_time = models.IntegerField()
    difficulty = models.CharField(max_length=25)
    description = models.TextField()
    # come back to define "upload_to"
    pic = pic = models.ImageField(upload_to='', default='no_picture.jpg')

    def __str__(self):
        return str(self.name)

# Create your models here.
