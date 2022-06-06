from django.db import models


# Create your models here.

class Users(models.Model):
    id = models.AutoField(verbose_name="id",primary_key=True)
    name = models.CharField(max_length=30, verbose_name="用户名")
    password = models.CharField(max_length=128, verbose_name="密码")
    
    def __str__(self):
        return self.name
