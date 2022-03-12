from rest_framework import generics
from etherium_api.serializers import TokenSerializer
from etherium_api.models import Tokens
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import services


class TokenCreateView(generics.CreateAPIView):
    serializer_class = TokenSerializer


class TokenListView(generics.ListAPIView):
    serializer_class = TokenSerializer
    queryset = Tokens.objects.all()


@api_view(['GET'])
def total_supply(request):
    return Response({"result": services.totalSupply()})

