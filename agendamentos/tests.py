from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

# Create your tests here.

class TestsExemplo(APITestCase):
    def test_create_account(self):
        """
        Modelo de Teste para o sistema
        """
        #url = reverse('account-list')
        #data = {'name': 'DabApps'}
        #response = self.client.post(url, data, format='json')
        #self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #self.assertEqual(Account.objects.count(), 1)
        #self.assertEqual(Account.objects.get().name, 'DabApps')
        self.assertEqual(2, 2)

    def test_chamada_pessoas(self):
        """
        Modelo de Teste para simples Get em pessoas
        """
        #factory = APIRequestFactory()
        #request = factory.get('/api/pessoas/')
        result = self.client.get(path='/api/pessoas/')
        print("Resultado do get:")
        print(result.data)
        self.assertEqual(result.status_code, status.HTTP_200_OK)


        