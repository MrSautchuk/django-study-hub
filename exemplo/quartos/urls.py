from django.urls import path
from . import views

app_name = 'quartos'
urlpatterns = [
    path('quartos/', views.lista_quartos, name='lista'),
    path('quartos/novo/', views.criar_quarto, name='criar'),
    path('quartos/<int:pk>/', views.detalhe_quarto, name='detalhe'),
]
