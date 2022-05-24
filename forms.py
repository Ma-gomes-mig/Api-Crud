from django import forms
from .models import Funcionario

class FuncionarioModelForm(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields = '__all__'