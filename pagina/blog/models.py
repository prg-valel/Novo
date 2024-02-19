from django.db import models

class Publi(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.CharField(max_length=200)
    data = models.DateField()
    conteudo = models.TextField()