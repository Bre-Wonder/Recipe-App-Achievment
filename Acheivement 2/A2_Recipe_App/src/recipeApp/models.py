from django.db import models


class Recipe(models.Model):
    id =
    name = models.CharField(max_length=120)
    ingredients =
    cooking_time =
    difficulty =
    description = models.TextField()

    def __str__(self):
        return str(self.name)

# Create your models here.
