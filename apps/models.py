# chat/models.py
from django.db import models
from django.db.models import Model
from django.db.models.fields import CharField


# Create your models here.

class Category(Model):
    title = CharField(max_length=255)


class Students(Model):
    name = CharField(max_length=255),
