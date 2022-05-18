from rest_framework import status
from agendamentos.models import Servico, Pessoa
from rest_framework.test import APITestCase


# Create your tests here.

class TestsExemplo(APITestCase):

    def __init__(self, *args, **kwargs):
        super(TestsExemplo, self).__init__(*args, **kwargs)                

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
         result = self.client.get(path='/api/pessoas/') 
         self.assertNotEqual(result.status_code, status.HTTP_200_OK)

    def testa_autenticao(self):         
        p = Pessoa()         
        p.first_name="teste"
        p.last_name="teste"
        p.username = "teste5"
        p.nome = "Teste5"  
        p.email = "teste@teste.com"
        p.new_password = "teste5"
        p.cpf = "1231231230X"
        p.is_active = True
        p.save()
        result = self.client.post('/api/token/', {'username': 'teste5', 'password': 'teste5'})
        self.assertIn(result.status_code,range(200,299))
    
    def testa_bloqueio_recurso_de_client_autenticado(self):
        p = Pessoa()         
        p.first_name="teste"
        p.last_name="teste"
        p.username = "teste5"
        p.nome = "Teste5"  
        p.email = "teste@teste.com"
        p.new_password = "teste5"
        p.cpf = "1231231230X"
        p.is_active = True
        p.save()
        token = self.client.post('/api/token/', {'username': 'teste5', 'password': 'teste5'}).data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        result  = self.client.get('/api/pessoas/')
        self.assertNotIn(result.status_code, range(200,299))
        result  = self.client.get('/api/servicos/')
        self.assertIn(result.status_code, range(200,299))
        
        

         
         
         
        
