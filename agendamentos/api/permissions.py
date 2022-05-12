from rest_framework import permissions, generics
from django.http import HttpRequest
from agendamentos.models import Pessoa, Agendamento
import agendamentos.api.viewsets as viewsets



#Permmissão apenas se for gerente
class IsGerente(permissions.BasePermission):
    """
    Verifica se usuario possui credencial de gerente para atuar
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.is_gerente or request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return True
        return False

#Permissão se for atendente
class IsAtendente(permissions.BasePermission):
    """
    Verifica se usuario possui credencial de atendente para atuar
    """
    def has_permission(self, request, view):
        return request.user and (request.user.is_atendente or request.user.is_gerente or request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return True
        return False


class IsValidClientAction(permissions.BasePermission):
    """
    Verifica se o cliente esta fazendo acesso as views:
    -Caso logado permite alterar apenas seus dados pessoais e realizar ou alterar seu agendamento
    -Caso usuário não tenha logado, unica permissão será a criação de usuario na view de Pessoas
    """

    def has_permission(self, request, view):
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
        else:
            return True

class IsTeste(permissions.BasePermission):
    """
    Permis~são de exempl onde has_permission verificar se usuario pode acessar aquela view e 
    has_object_permission verificar se o objeto pode ser acessado depois de aprovado em has_permission
    """
    def has_permission(self, request: HttpRequest, view:generics.GenericAPIView):
        return True

    def has_object_permission(self, request:HttpRequest, view:generics.GenericAPIView, obj):
        print("Debug objeto permissoes")
        print(obj)
        print("view")
        print(view)
        return False

#outro exemplo de código verificado em fóruns
class BlocklistPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request: HttpRequest, view):
        ip_addr = request.META['REMOTE_ADDR']
        blocked = Blocklist.objects.filter(ip_addr=ip_addr).exists()
        user: Pessoa = request.user

        return not blocked
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return True
        return False