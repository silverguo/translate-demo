from django.db import models

# Create your models here.

class Translate(models.Model):
    lang_src = models.CharField(max_length=20)
    lang_tgt = models.CharField(max_length=20)
    model_id = models.CharField(max_length=4)
    record_src = models.TextField(default='')
    record_tgt = models.TextField(default='')
