from django.db import models

class Book(models.Model):
    id_book = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=100)
    link_access = models.CharField(max_length=100)
    date_record = models.DateField()