from django.db import models

# Create your models here.

class users(models.Model):
    username=models.CharField(max_length=15)
    key=models.CharField(max_length=25)
    email=models.EmailField(max_length=25)
    joined=models.DateTimeField(auto_now_add=True)
    mobile=models.IntegerField()

    def __str__(self):
        return self.username


