from rest_framework import serializers, viewsets
from .models import Quarto

class QuartoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quarto
        fields = ['id', 'numero', 'tipo', 'disponivel']

class QuartoViewSet(viewsets.ModelViewSet):
    queryset = Quarto.objects.all().order_by('numero')
    serializer_class = QuartoSerializer
