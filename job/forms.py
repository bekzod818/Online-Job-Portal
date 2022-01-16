from django.forms import ModelForm, FileInput
from .models import *


class ApplyForm(ModelForm):
    class Meta:
        model = Candidates
        fields = "__all__"

    # widgets = {
    #     'resume': FileInput(attrs={
    #         'class': 'form-control'
    #     })
    # }