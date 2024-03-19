from django.db import models
from app import views
from credentials import MpesaAccessToken, LipanaMpesaPpassword

# Create your models here.


class Client(models.Model):
    number=models.CharField(max_length=10, blank=False, null=False)
    amount=models.CharField()


    def __str__(self):
        return self.number
