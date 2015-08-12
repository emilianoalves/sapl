from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

import json

from parlamentares.models import Parlamentar
from sessao.models import SessaoPlenaria, SessaoPlenariaPresenca, PresencaOrdemDia, RegistroVotacao, VotoParlamentar, OrdemDia, PresencaOrdemDia

# REST web services
def json_presenca(request):
   presencas = PresencaOrdemDia.objects.filter(sessao_plenaria_id = 50)
   parlamentares = []
   for p in presencas:
      parlamentares.append(p.parlamentar)
   #parlamentares = serializers.serialize('json', Parlamentar.objects.all())
   parlamentares = serializers.serialize('json', parlamentares)
   return HttpResponse(parlamentares,  content_type='application/json')
   #return JsonResponse(data) # work with python dict

def json_votacao(request):
    #TODO: se tentar usar objects.get(ordem_id = 104 ocorre a msg: 'RegistroVotacao' object does not support indexing
    #TODO; tratar o caso de vir vazio
    votacao = RegistroVotacao.objects.filter(ordem_id = 104)[0]

    # Magic! http://stackoverflow.com/questions/15507171/django-filter-query-foreign-key
    voto_parlamentar = VotoParlamentar.objects.filter(votacao__ordem__id = 140)

    ordem_dia = OrdemDia.objects.get(id = 104)

    sessaoplenaria_id = ordem_dia.sessao_plenaria_id

    sessao_plenaria = SessaoPlenaria.objects.get(id = sessaoplenaria_id)

    presenca_ordem_dia = PresencaOrdemDia.objects.filter(sessao_plenaria_id = sessaoplenaria_id)
    presentes_ordem_dia = []
    for p in presenca_ordem_dia:
        presentes_ordem_dia.append(p.parlamentar.nome_parlamentar)
    presentes_ordem_dia.sort()
    total_votos = votacao.numero_votos_sim + votacao.numero_votos_nao + votacao.numero_abstencoes

    sessao_plenaria_presenca = SessaoPlenariaPresenca.objects.filter(id = sessaoplenaria_id)
    presentes_sessao_plenaria = []
    for p in sessao_plenaria_presenca:
        presentes_sessao_plenaria.append(p.parlamentar.nome_parlamentar)

    votacao_json = {"sessao_plenaria": str(sessao_plenaria),
                    "sessao_plenaria_data": sessao_plenaria.data_inicio,
                    "sessao_plenaria_hora_inicio": sessao_plenaria.hora_inicio,
                    "materia_legislativa_texto": ordem_dia.materia.ementa,
                    "observacao_materia": ordem_dia.materia.observacao,
                    "tipo_votacao": ordem_dia.tipo_votacao, # TODO: verbose name
                    "numero_votos_sim": votacao.numero_votos_sim,
                    "numero_votos_nao": votacao.numero_votos_nao,
                    "numero_abstencoes": votacao.numero_abstencoes,
                    "total_votos": total_votos,
                    "tipo_resultado": votacao.tipo_resultado_votacao.nome.upper(),
                    "presentes_ordem_dia": presentes_ordem_dia,
                    "presentes_sessao_plenaria": presentes_sessao_plenaria,
                   }
    return JsonResponse(votacao_json)

# UI views
def painel_view(request):
    context = {'head_title': 'Painel Plenário', 'title': '3a. Sessao Ordinária do Município XYZ'}
    return render(request, 'painel/index.html', {'context': context})

def painel_parlamentares_view(request):
    return render(request, 'painel/parlamentares.html')

def painel_votacao_view(request):
    return render(request, 'painel/votacao.html')
