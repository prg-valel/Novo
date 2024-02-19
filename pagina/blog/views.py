from django.shortcuts import render
from .models import Publi
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from datetime import datetime


def feed_page(request):
    publis = Publi.objects.all()
    return render(request, "feed.html", {
        'publis' : publis
    })

def publicate_page(request):
    if request.method == 'GET':
        return render(request, "publicate.html")
    elif request.method == 'POST':
        autor = request.POST.get('autor')
        data = datetime.today()
        conteudo = request.POST.get('conteudo')
        publi = Publi()
        publi.autor = autor
        publi.data = data
        publi.conteudo = conteudo
        publi.save()
        return HttpResponseRedirect('/feed')
    else:
        return HttpResponseBadRequest()
