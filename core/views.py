from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from core.models import Marca, Categoria, Carro
from core.serializers import MarcaSerializer, CategoriaSerializer, CarroSerializer


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
