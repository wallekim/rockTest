from django.db import models
import hashlib
import time


def _createHash():
    """This function generate 10 character long hash"""
    hash = hashlib.sha1()
    hash.update(str(time.time()))
    return hash.hexdigest()[:-20]


class Tokens(models.Model):
    unique_hash = models.CharField(max_length=20, default=_createHash,unique=True)
    tx_hash = models.CharField(max_length=20, default=_createHash,unique=True)
    link_to_media = models.FileField(verbose_name='Link to media', upload_to='media/')
    owner = models.URLField(max_length=500,)

    class Meta:
        verbose_name = 'token'
        verbose_name_plural = 'tokens'