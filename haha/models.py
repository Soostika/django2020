from django.db import models

# Create your models here.
class table(models.Model):
    name = models.CharField(max_length=233,blank =True, null=True)
    address = models.CharField(max_length=233,blank =True, null=True)

    def __str__(self):

        return f"{self.name}"