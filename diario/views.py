from datetime import datetime, timedelta

from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect
from collections import Counter

from .models import Pessoa, Diario


def home(request):
    textos = Diario.objects.all().order_by('-create_at')[:3]

    pessoas_com_contagem = Pessoa.objects.annotate(qtd_diarios=Count('diario'))
    nomes = [pessoa.nome for pessoa in pessoas_com_contagem]
    qtds = [pessoa.qtd_diarios for pessoa in pessoas_com_contagem]

    todas_as_tags = []
    for diario in Diario.objects.all():
        if diario.tags:
            todas_as_tags.extend(diario.tags.split(','))

    contagem_tags = Counter(todas_as_tags)
    tags = list(contagem_tags.keys())
    qtd_tags = list(contagem_tags.values())

    return render(request, 'home.html', {
        'textos':textos,
        'nomes':nomes,
        'qtds':qtds,
        'tags':tags,
        'qtd_tags':qtd_tags})

def escrever(request):
    if request.method == 'GET':
        pessoas = Pessoa.objects.all()

        return render(request, 'escrever.html', {'pessoas':pessoas})

    elif request.method == 'POST':

        titulo  = request.POST.get('titulo')
        tags    = request.POST.getlist('tags')
        pessoas = request.POST.getlist('pessoas')
        texto   = request.POST.get('texto')

        if len(titulo.strip()) == 0 or len(texto.strip()) == 0:
            return render(request, 'escrever.html', {
                'pessoas': Pessoa.objects.all(),
                'error_message': 'Título e texto não podem estar vazios!'
            })

        diario = Diario(titulo=titulo, texto=texto)
        diario.save()

        for i in pessoas:
            pessoa = Pessoa.objects.get(id = i)
            diario.pessoas.add(pessoa)

        diario.set_tags(tags)
        diario.save()

        return render(request, 'escrever.html', {
            'pessoas': Pessoa.objects.all(),
            'sucess_message': 'Registro diário salvo com sucesso!'
        })


def cadastrar_pessoa(request):
    if request.method == 'GET':
        return render(request, 'pessoa.html')

    elif request.method == 'POST':

        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')

        pessoa = Pessoa(nome=nome, foto=foto)
        pessoa.save()

        return redirect('escrever')

def dia(request):
    data = request.GET.get('data')
    data_formatada = datetime.strptime(data, '%Y-%m-%d')

    diarios = (Diario.objects.filter(create_at__gte=data_formatada)
              .filter(create_at__lte=data_formatada + timedelta(days=1)))


    return render(request, 'dia.html', {'diarios':diarios, 'total':diarios.count(), 'data':data})

def excluir_dia(request):
    dia = datetime.strptime(request.GET.get('data'),'%Y-%m-%d')
    diarios = (Diario.objects.filter(create_at__gte=dia)
               .filter(create_at__lte=dia + timedelta(days=1)))

    diarios.delete()

    return HttpResponse('teste')