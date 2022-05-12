from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from agendamentos.models import Servico, Pessoa

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
           

    def bloqueio_listagem_clientes_sem_autenticacao(self):
         p = Pessoa()
         p.nome = "Teste"  
         p.email = "teste@teste.com"
         p.new_password = "teste"
         p.save()
         result = self.client.get(path='/api/pessoas/') 
         self.assertNotEqual(result.status_code, status.HTTP_200_OK)

        
