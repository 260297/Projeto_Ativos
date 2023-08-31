from django import forms
from .models import Ativos,Manutencoes

class AtivosForm(forms.ModelForm):
    class Meta:
        model = Ativos
        fields = '__all__'  # Inclui todos os campos do modelo no formulário
    

class ManutencaoForm(forms.ModelForm):
    class Meta:
        model = Manutencoes
        fields = ['imob', 'ativo', 'data_manutencao', 'descricao', 'tecnico_responsavel']
