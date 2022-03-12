from django.db import models


class Tokens(models.Model):
    unique_hash = models.CharField(max_length=20, unique=True, blank=True)
    tx_hash = models.TextField()
    link_to_media = models.URLField(verbose_name='Link to media')
    owner = models.CharField(max_length=1000,)

    class Meta:
        verbose_name = 'token'
        verbose_name_plural = 'tokens'