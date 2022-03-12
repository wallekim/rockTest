from rest_framework import serializers
from etherium_api.models import Tokens
from rest_framework.response import Response
from etherium_api.services import random_md5like_hash, change_contract_state


class TokenSerializer(serializers.ModelSerializer):
    unique_hash = serializers.CharField(read_only=True)
    tx_hash = serializers.CharField(read_only=True)

    class Meta:
        model = Tokens
        fields = '__all__'

    def create(self, validated_data):
        random_hash = random_md5like_hash()
        token = Tokens.objects.create(
            owner=validated_data.get("owner"),
            link_to_media=validated_data.get("link_to_media"),
            unique_hash=random_hash,
            tx_hash=change_contract_state(validated_data.get("owner"), random_hash,
                                          validated_data.get("link_to_media"))
        )
        token.save()
        return token

