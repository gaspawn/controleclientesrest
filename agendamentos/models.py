# Create your models here.
# Arquivo em ficam registrados os os objetos para o banco de dados
from django.db import models
from django.db.models.fields import CharField
from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth.models import User
import datetime 

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=11, validators=[
                           RegexValidator(regex='[0-9]{11}')],unique=True, null=False) #é um validador de expressão regular???
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    nome = models.CharField(max_length=200,null=False)
    endereco = models.CharField(max_length=200,null=True)
    nascimento = models.DateField('data de nascimento',null=True)
    telefone = models.CharField(max_length=15,null=True)
    email = models.CharField(max_length=50,null=True)

    def get_user(self)-> User:
        return User.objects.get(id=self.user)

    def __str__(self):
        return self.nome


class Servico(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200,null=False)
    descricao = models.CharField(max_length=200,null=False)
    duracao_prevista = models.IntegerField(default=30)
    ativo = models.BooleanField(default=True) #Utilizado para exclusão lógica

    def __str__(self):
        return self.nome


class Atendente(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    nome = models.CharField(max_length=200,null=False)

    def get_user(self)-> User:
        return User.objects.get(id=self.user)

    def __str__(self):
        return self.nome

##Array de controle de agendamentos
class Agendamento(models.Model):
    id = models.AutoField(primary_key=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE,null=False)
    dia:models.DateField = models.DateField(null=False)
    horario = models.TimeField()
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, null=False)
    atendente =  models.ForeignKey(Atendente, on_delete=models.CASCADE,null=False)

    def __str__(self):
        return self.id

    def dataNoFuturo(self)-> bool:
        today:datetime.date = datetime.date.today()
        return True if today < self.dia else False

