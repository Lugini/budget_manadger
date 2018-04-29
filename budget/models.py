from django.db import models as model
from django.contrib.auth.models import *

class Budget(model.Model):
    budget = models.IntegerField(default=0)
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Budget'


class Transfer(model.Model):
    amount=model.FloatField(default=0)
    date=model.DateTimeField(auto_now=True)
    title=model.CharField(max_length=200)
