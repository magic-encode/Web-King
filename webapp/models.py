from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=255, )
    age = models.IntegerField()
    cours = models.CharField(max_length=255, )
    numbers = models.PositiveBigIntegerField()
    numbers_parent = models.PositiveBigIntegerField()
    text = models.TextField()
    
    def __str__(self) -> str:
        return self.name
