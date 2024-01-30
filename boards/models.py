from django.db import models
from django.db.models import JSONField

class Board(models.Model):
    name = models.CharField(max_length=255)

class Report(models.Model):
    name = models.CharField(max_length=255)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='reports')
    data = JSONField(default=dict)
