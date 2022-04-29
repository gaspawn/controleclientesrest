# Create your models here.
# Arquivo em ficam registrados os os objetos para o banco de dados
from django.db import models
from django.db.models.fields import CharField
from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth.models import User 
from django.contrib.auth.models import AbstractUser
import datetime 

class Pessoa(AbstractUser):    
    cpf = models.CharField(max_length=11, validators=[
                           RegexValidator(regex='[0-9]{11}')],unique=True, null=False) #é um validador de expressão regular???        
    endereco = models.CharField(max_length=200,null=True)
    nascimento = models.DateField('data de nascimento',null=True)
    telefone = models.CharField(max_length=15,null=True)    
    is_atendente = models.BooleanField(default=False)
    is_gerente = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    def nome_completo(self)->str:
        return self.first_name + ' ' + self.last_name


class Servico(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200,null=False,blank=False)
    descricao = models.CharField(max_length=200,null=False)
    duracao_prevista = models.IntegerField(default=30)
    ativo = models.BooleanField(default=True) #Utilizado para exclusão lógica

    def __str__(self):
        return self.nome


##Array de controle de agendamentos
class Agendamento(models.Model):
    id = models.AutoField(primary_key=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE,null=False,related_name='pessoa_fk')
    dia:models.DateField = models.DateField(null=False)
    horario = models.TimeField()
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, null=False)
    atendente =  models.ForeignKey(Pessoa, on_delete=models.CASCADE,null=False,related_name='atendente_fk')

    def __str__(self):
        return self.id

   
