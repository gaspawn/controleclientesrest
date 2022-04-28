from django.urls import path, include
from rest_framework import routers
from agendamentos.api.viewsets import PessoaViewSet, AtendenteViewSet, AgendamentoViewSet, ServicoViewSet


router = routers.DefaultRouter()

router.register(r'pessoas', PessoaViewSet, basename='pessoa')
router.register(r'servicos', ServicoViewSet, basename='servico')
router.register(r'atendentes', AtendenteViewSet, basename='atendente')
router.register(r'agendamentos', AgendamentoViewSet, basename='agendamento')

urlpatterns = [
    path('api/', include(router.urls)),
]

