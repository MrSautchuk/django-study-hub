from django import forms
from .models import Quarto

class QuartoForm(forms.ModelForm):
    class Meta:
        model = Quarto
        fields = ['numero', 'tipo', 'disponivel']

    def clean_numero(self):
        numero = self.cleaned_data['numero']
        if numero < 1:
            raise forms.ValidationError('O número deve ser maior que zero.')
        return numero
