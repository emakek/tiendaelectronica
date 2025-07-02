from django.shortcuts import render
from .models import Producto

def galeria_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/galeria.html', {'productos': productos})

# productos/views.py

from django.shortcuts import render, redirect
from .forms import ContactoForm

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto')  # redirige a la misma página u otra
    else:
        form = ContactoForm()
    return render(request, 'productos/contacto.html', {'form': form})