from django.urls import path
from .views import IndexView, CreateFuncionarioView, UpdateFuncionarioView, DeleteFuncionarioView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cadastrar/', CreateFuncionarioView.as_view(), name='cadastra_funcionario'),
    path('<pk>/update/', UpdateFuncionarioView.as_view(), name='upd_funcionario'),
    path('<pk>/delete/', DeleteFuncionarioView.as_view(), name='del_funcionario'),
]