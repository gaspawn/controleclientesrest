from rest_framework import permissions, generics
from django.http import HttpRequest
from agendamentos.models import Pessoa, Agendamento
import agendamentos.api.viewsets as viewsets


class IsValidClientAction(permissions.BasePermission):
    """
    Verifica se o cliente esta fazendo acesso as views:
    -Caso logado permite alterar apenas seus dados pessoais e realizar ou alterar seu agendamento
    -Caso usuário não tenha logado, unica permissão será a criação de usuario na view de Pessoas
    """

    def has_permission(self, request, view):
        """
           Verifica se o usuário pode ao menos chamar a view
        """
        self.verifica_seguranca_criacao_usuario(request, view)
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
        user: Pessoa = request.user
        if user.is_authenticated and ( not user.is_gerente and  not user.is_atendente and not user.is_superuser):
            if type(view) == viewsets.AgendamentoViewSet:
                agendamento: Agendamento = obj
                return True if agendamento.pessoa in [user, None] else False #cliente só altera agendamento em branco para ele ou dele mesmo
            elif type(view) == viewsets.PessoaViewSet:
                pessoa: Pessoa = obj
                return True if pessoa == user else False #cliente só altera seus dados pessoais
            return True
        #else:
        #    return True
        elif user.is_gerente or user.is_atendente or user.is_superuser:
            return True
        return False

    def verifica_seguranca_criacao_usuario(self, request:HttpRequest, view):
        """
        Verifica se o usuario que não é gerente esta tentando criar novos atendentes ou gerentes, permitindo apenas que atendente set esta flag quando se
        tratar dele mesmo
        """
        user:Pessoa  = request.user
        if type(view) == viewsets.PessoaViewSet and view.action in ['create','update','partital_update'] \
            and (request.POST['is_atendente']  == true or request.POST['is_gerente'] == true):
            if user.is_authenticated and (user.is_gerente or user.is_superuser):
                return True
            elif user.is_authenticated and user.is_atendente and not request.POST['is_gerente'] == 'true' \
                and user.id == int(request.POST['id']):
                return True                                
            else:
                return False
        return True

                





