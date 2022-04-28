from django.contrib import admin
from agendamentos.models import Pessoa, Atendente, Servico, Agendamento
# Register your models here.
admin.register(Pessoa)
admin.register(Atendente)
admin.register(Servico)
admin.register(Agendamento)