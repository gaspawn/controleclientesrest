from django.contrib import admin
from agendamentos.models import Pessoa, Servico, Agendamento
# Register your models here.
admin.register(Pessoa)
admin.register(Servico)
admin.register(Agendamento)