from operator import truediv
from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=200)

    def  __str__(self):  
        return self.username

class WebAppPassword(models.Model):
    webapp_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=200)
    web_address = models.CharField(max_length=30)
    note = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.title



class CardPassword(models.Model):
    card_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=20)
    card_holder_name = models.CharField(max_length=20)
    card_number = models.CharField(max_length=19)
    card_exp = models.CharField(max_length=20)
    card_cvv = models.CharField(max_length=200)
    card_atm_pin = models.CharField(max_length=200)

    def __str__(self):
        return self.card_holder_name