"""
Esta classe será utilizada para mapear o token de autenticação do usuário na urls.py para permitir
incluir no token outros atributos que o desenvolvedor precisar
"""

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user:User):
        token = super().get_token(user)

        token['username'] = user.name
        token['nome'] = user.first_name #Substituir por nome da tabela pessoa
        token['groups'] = user.groups.all()
        # ...
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer