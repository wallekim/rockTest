from rest_framework import generics
from etherium_api.serializers import TokenSerializer
from etherium_api.models import Tokens


class TokenCreateView(generics.CreateAPIView):
    serializer_class = TokenSerializer


class TokenListView(generics.ListAPIView):
    serializer_class = TokenSerializer
    queryset = Tokens.objects.all()


# Create your views here.
