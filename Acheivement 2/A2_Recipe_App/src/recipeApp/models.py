from django.db import models


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=255)
    cooking_time = models.IntegerField()
    difficulty = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return str(self.name)

# Create your models here.
