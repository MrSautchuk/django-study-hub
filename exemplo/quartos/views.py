from django.shortcuts import get_object_or_404, redirect, render
from .forms import QuartoForm
from .models import Quarto

def lista_quartos(request):
    quartos = Quarto.objects.filter(disponivel=True).order_by('numero')
    return render(request, 'quartos/lista.html', {'quartos': quartos})

def detalhe_quarto(request, pk):
    quarto = get_object_or_404(Quarto, pk=pk)
    return render(request, 'quartos/detalhe.html', {'quarto': quarto})

def criar_quarto(request):
    form = QuartoForm(request.POST if request.method == 'POST' else None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('quartos:lista')
    return render(request, 'quartos/form.html', {'form': form})
