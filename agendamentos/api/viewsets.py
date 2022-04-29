#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from agendamentos.models import Pessoa, Agendamento, Servico
from agendamentos.api.serializers import PessoaSerializer, ServicoSerializer, AgendamentoSerializer


from agendamentos.api import serializers


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    #permission_classes = [permissions.IsAuthenticated]


class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    #permission_classes = [permissions.IsAuthenticated]    

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    #permission_classes = [permissions.IsAuthenticated]



""" 
Para criar APIS personalizadas para o Django Rest Framework, não derivadas do ModelViewSet diretamente
"""
class TesteApi(APIView):
    def get(self, request, format=None):
        return JsonResponse({'message':'Hello World'})
