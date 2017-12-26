from django.db import models

# Create your models here.

class Translate(models.Model):
    lang_src = models.CharField(max_length=20, 
                                default='')
    lang_tgt = models.CharField(max_length=20, 
                                default='')
    record_src = models.TextField(default='')
    record_tgt = models.TextField(default='')
