from django.db import models
from etherium_api import services
import hashlib
import time


def _createHash():
    """This function generate 10 character long hash"""
    hash_ = hashlib.sha1()
    hash_.update(str(time.time()))
    return hash_.hexdigest()[:-20]


class Tokens(models.Model):
    unique_hash = models.CharField(max_length=20, default=_createHash, unique=True)
    tx_hash = models.CharField(max_length=20)
    link_to_media = models.URLField(verbose_name='Link to media')
    owner = models.CharField(max_length=500,)

    class Meta:
        verbose_name = 'token'
        verbose_name_plural = 'tokens'