from rest_framework import serializers

from core.models import Marca, Categoria, Carro


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = "__all__"
