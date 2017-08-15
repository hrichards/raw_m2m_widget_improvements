from django.db import models


class ModelB(models.Model):
    pass


class ModelA(models.Model):
    model_b = models.ForeignKey(ModelB, null=True, blank=True, on_delete=models.SET_NULL, related_name='foos')
    model_bs = models.ManyToManyField(ModelB)
