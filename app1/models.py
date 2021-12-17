from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title=models.CharField(max_length=30)
    vaqt=models.TimeField()
    joy=models.CharField(max_length=20,blank=True)
    description=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    foydalanuvchi=models.OneToOneField(User,on_delete=models.CASGADE)

    def __str__(self):
        return f"{self.title},{self.status}"

