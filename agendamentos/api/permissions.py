from rest_framework import permissions
from django.http import HttpRequest
from models import Pessoa

class BlocklistPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request: HttpRequest, view):
        ip_addr = request.META['REMOTE_ADDR']
        blocked = Blocklist.objects.filter(ip_addr=ip_addr).exists()
        user: Pessoa = request.user

        return not blocked

#Permmissão apenas se for gerente
class IsGerente(permissions.BasePermission):
    """
    Allows access only to "is_active" users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_gerente

#Permissão se for atendente
class IsAtendente(permissions.BasePermission):
    """
    Allows access only to "is_active" users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_atendente

