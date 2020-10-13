from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Categorias

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categorias
        fields = ('id_categoria','categoria')