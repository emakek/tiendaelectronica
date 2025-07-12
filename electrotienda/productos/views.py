from django.shortcuts import render
from .models import Producto

def galeria_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/galeria.html', {'productos': productos})

# productos/views.py

from django.shortcuts import render, redirect
from .forms import ContactoForm

from django.shortcuts import render, redirect
from .forms import ContactoForm

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto')  # O puedes redirigir a una página de éxito
    else:
        form = ContactoForm()
    return render(request, 'productos/contacto.html', {'form': form})

def inicio(request):
    return render(request, 'productos/inicio.html')