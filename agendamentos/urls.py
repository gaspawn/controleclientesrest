from django.urls import path, include
from rest_framework import routers
from agendamentos.api.viewsets import PessoaViewSet, AgendamentoViewSet, ServicoViewSet, TesteApi
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()

router.register(r'pessoas', PessoaViewSet, basename='pessoa')
router.register(r'servicos', ServicoViewSet, basename='servico')
router.register(r'agendamentos', AgendamentoViewSet, basename='agendamento')

urlpatterns = [
    path('teste', TesteApi.as_view(), name='teste'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),
]

