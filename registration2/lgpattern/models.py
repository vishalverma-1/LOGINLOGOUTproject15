from django.db import models
class vishal(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    mobile=models.BigIntegerField(max_length=20)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.name
