"""
Esta classe será utilizada para mapear o token de autenticação do usuário na urls.py para permitir
incluir no token outros atributos que o desenvolvedor precisar
"""

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from agendamentos.models import Pessoa

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user:Pessoa):
        token = super().get_token(user)

        token['username'] = user.username
        token['nome'] = user.first_name #Substituir por nome da tabela pessoa
        token['email'] = user.email        
        token['is_atendente'] = user.is_atendente
        token['is_gerente'] = user.is_gerente
        # ...
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer