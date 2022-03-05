from django.db import models

# Create your models here.
class saveFile(models.Model):
    name=models.CharField(max_length=50)
    message=models.TextField()
    fname=models.FileField(upload_to='files/',max_length=250,null=True,default=None)
