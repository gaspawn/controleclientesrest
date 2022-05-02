#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from agendamentos.models import Pessoa, Agendamento, Servico
from agendamentos.api.serializers import PessoaSerializer, ServicoSerializer, AgendamentoSerializer
from rest_framework import status
from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
import urllib
from datetime import datetime


from agendamentos.api import serializers


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    #permission_classes = [permissions.IsAuthenticated]


class AgendamentoViewSet(viewsets.ModelViewSet):
    #queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    #permission_classes = [permissions.IsAuthenticated]    
    def get_queryset(self):
        """
        Sobrescre o metodo get para aceitar o parametro dia no intuito de filtrar a agenda para o dia especifico
        """
        queryset = Agendamento.objects.all()
        dia = self.request.query_params.get('dia', None).replace('/','')
        if dia is not None:
            try:
                dia = urllib.parse.unquote(dia)
                dt = str.split(dia,"T")[0]
                dt = datetime.strptime(dt, '%Y-%m-%d')
                queryset = queryset.filter(dia=dt)
            except:
                raise serializers.ValidationError('Dia invalido')
        return queryset

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    #permission_classes = [permissions.IsAuthenticated]



class Agenda(APIView):
    def get(self, request, format=None):
        agenda = Agendamento.objects.all()
        serializer = AgendamentoSerializer(agenda, many=True)
        return Response(serializer.data)

    def get(self,request,pk,format=None): #Método para lista todos agendamentos do dia em pk no formato json/javascript
        #pk no formato YYYY-MM-DD
        agenda = Agendamento.objects.get(pk=pk)
        serializer = AgendamentoSerializer(agenda)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


""" 
Para criar APIS personalizadas para o Django Rest Framework, não derivadas do ModelViewSet diretamente
"""
class TesteApi(APIView):
    def get(self, request, format=None):
        return JsonResponse({'message':'Hello World'})

""" Exemplo de generic view para implementar compativel com router e documentação 
class ItemViewSet(GenericViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = [DjangoObjectPermissions]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return self.get_paginated_response(self.paginate_queryset(serializer.data))

    def retrieve(self, request, pk):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def destroy(self, request):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        """