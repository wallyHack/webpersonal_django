from django.shortcuts import render
from .models import Proyecto

# Create your views here.
def portfolio(request):
    # obtenemos todos los proyectos y los enviamos a la plantilla
    lista_proyectos = Proyecto.objects.all()    
    context = {'lista_proyectos': lista_proyectos}
    return render(request, 'portfolio/portfolio.html', context)