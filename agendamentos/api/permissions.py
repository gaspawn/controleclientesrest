from rest_framework import permissions, generics
from django.http import HttpRequest
from agendamentos.models import Pessoa, Agendamento
import agendamentos.api.viewsets as viewsets
from decouple import config

class IsValidClientAction(permissions.BasePermission):
    """
    Verifica se o cliente esta fazendo acesso as views:
    -Caso logado permite alterar apenas seus dados pessoais e realizar ou alterar seu agendamento
    -Caso usuário não tenha logado, unica permissão será a criação de usuario na view de Pessoas
    """

    def has_permission(self, request, view):
        if not config('AUTENTICAR', default=False, cast=bool):
            print("Autenticação desabilitada, habilitar em settings.py AUTENTICAR")
            return True
        if request.user.is_authenticated:
            if request.user.is_gerente or request.user.is_atendente or request.user.is_superuser:
                return True
            else:
                if view.action in ['update', 'partial_update' 'retrieve'] and type(view) in [viewsets.PessoaViewSet,viewsets.AgendamentoViewSet]:
                    return True
                elif view.action in ['list','retrieve'] and type(view) != viewsets.PessoaViewSet:
                    return True
                else:
                    return False
        else: #Usuário que não está autenticado é permitido apenas criar ou seu perfil
            return True if view.action in ['create'] and type(view) == viewsets.PessoaViewSet else False                

    def has_object_permission(self, request, view, obj):        
        """
        Verifica se o usuario esta autenticado e se é o mesmo que esta tentando alterar seu agendamento ou seus dados em pessoa
        """
        if not config('AUTENTICAR', default=False, cast=bool):
            return True
        user: Pessoa = request.user
        if user.is_authenticated and ( not user.is_gerente and  not user.is_atendente and not user.is_superuser):
            if type(view) == viewsets.AgendamentoViewSet:
                agendamento: Agendamento = obj
                return True if agendamento.pessoa in [user, None] else False #cliente só altera agendamento em branco para ele ou dele mesmo
            elif type(view) == viewsets.PessoaViewSet:
                pessoa: Pessoa = obj
                return True if pessoa == user else False #cliente só altera seus dados pessoais
            return True
        else:
            return True

