from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Funcionario
from .forms import FuncionarioModelForm
from django.urls import reverse_lazy


class IndexView(ListView):
    model = Funcionario
    template_name = 'index.html'
    queryset = Funcionario.objects.all()
    context_object_name = 'funcionarios'

class CreateFuncionarioView(CreateView):
    model = Funcionario
    template_name = 'funcionario_cadastra.html'
    fields = '__all__'
    success_url = reverse_lazy('index')


class UpdateFuncionarioView(UpdateView):
    model = Funcionario
    template_name = 'funcionario_form.html'
    fields = '__all__'
    success_url = reverse_lazy('index')

class DeleteFuncionarioView(DeleteView):
    model = Funcionario
    template_name = 'funcionario_del.html'
    success_url = reverse_lazy('index')