from multiprocessing import context
from django.shortcuts import render
from .models import familiar


def persona(request):
    mi_familiar = familiar.objects.create(name='Fabian', birth='1959-12-23', dni='12345678')
    contexto = {'familiar': mi_familiar}

    return render(request, 'familiar.html', contexto)

def ver_persona(request):
    mi_familiar = familiar.objects.all()
    contexto = {'familiar': mi_familiar}

    return render(request, 'familiar.html', contexto)