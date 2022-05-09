from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from agendamentos.models import Servico

# Create your tests here.

class TestsExemplo(APITestCase):
    def test_database_save(self):
        """
        Teste de Acesso ao banco de dados
        """
        servico = Servico()
        servico.nome = "Teste"
        servico.descricao = "Teste"
        servico.save()
        var_teste = Servico.objects.first()
        self.assertEqual(var_teste.nome, "Teste")
        

    def test_chamada_endpoint(self):
        """
        Teste de servidor e API - Verificar se a API esta funcionando
        """
        #factory = APIRequestFactory()
        #request = factory.get('/api/pessoas/')
        result = self.client.get(path='/api/pessoas/')
        print("Resultado do get:")
        print(result.data)
        self.assertEqual(result.status_code, status.HTTP_200_OK)


        