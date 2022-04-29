from rest_framework import serializers
from agendamentos.models import Pessoa, Agendamento, Servico


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        #fields = ('id', 'cpf', 'nome', 'endereco', 'nascimento', 'telefone', 'email')
        fields = '__all__'


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

