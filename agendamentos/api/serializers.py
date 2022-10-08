from rest_framework import serializers
from agendamentos.models import Pessoa, Agendamento, Servico, HistoricoPontosPessoa


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('id','username','cpf', 'first_name','last_name', 'endereco', 'nascimento', 'telefone', 'email','is_atendente','is_gerente','new_password')
        #fields = '__all__'

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        #fields = ('id', 'nome', 'descricao', 'duracao_prevista', 'ativo')
        fields = '__all__'

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        #fields = ('id', 'pessoa', 'dia', 'horario', 'servico', 'atendente')
        fields = '__all__'

class HistoricoPontosPessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoPontosPessoa
        fields = '__all__'

class SaldoPontosManagerSerializer(serializers.Serializer):
    id  = serializers.IntegerField(required=True)    
    saldo = serializers.IntegerField()
    