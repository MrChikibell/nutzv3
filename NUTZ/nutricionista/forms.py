from django import forms
from paciente.models import Paciente

class FormAddPaciente(forms.ModelForm):
    rut = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = Paciente
        fields = ['rut','email','nacionalidad','observacion','ultima_atencion','peso','glicemia_mgdl']
        # exclude = ['user', 'nutricionista']

