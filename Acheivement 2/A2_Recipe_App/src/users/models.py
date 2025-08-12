from django.db import models


class User(models.Model):
    id =
    username = models.CharField(max_length=120)

    def __str__(self):
        return str(self.name)

# Create your models here.
