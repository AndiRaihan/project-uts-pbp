from django import forms
from authen.models import Content

class TaskForms(forms.ModelForm):
    class Meta:
        model = Content
        fields = [
            'title',
            'description',
        ]