import pytest
from django.urls import reverse
from quartos.models import Quarto

@pytest.mark.django_db
def test_model():
    quarto = Quarto.objects.create(numero=101, tipo='Standard')
    assert str(quarto) == 'Quarto 101 — Standard'

@pytest.mark.django_db
def test_view_lista(client):
    Quarto.objects.create(numero=102, tipo='Luxo', disponivel=True)
    response = client.get(reverse('quartos:lista'))
    assert response.status_code == 200
    assert b'Luxo' in response.content

@pytest.mark.django_db
def test_api_post(client):
    response = client.post('/api/quartos/', data='{"numero": 103, "tipo": "Suite", "disponivel": true}', content_type='application/json')
    assert response.status_code == 201
    assert response.json()['numero'] == 103
    assert Quarto.objects.filter(numero=103).exists()
