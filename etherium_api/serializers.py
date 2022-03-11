from rest_framework import serializers
from etherium_api.models import Tokens


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tokens
        fields = ['link_to_media', 'owner']
