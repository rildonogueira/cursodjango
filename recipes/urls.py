from django.urls import path
from recipes.views import contato, home, sobre, compra, venda, troca

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
    path('compra/', compra),
    path('venda/', venda),
    path('troca/', troca),

]
