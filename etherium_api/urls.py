from etherium_api.views import TokenListView, TokenCreateView, total_supply
from django.urls import path

urlpatterns = [
    path('list/', TokenListView.as_view()),
    path('create/', TokenCreateView.as_view()),
    path('total_supply/', total_supply)
               ]