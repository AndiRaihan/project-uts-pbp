from django import forms
from authen.models import Content
from forum.models import Forum

class TaskForms(forms.ModelForm):
    class Meta:
        model = Content
        fields = [
            'title',
            'description',
        ]

class GroupForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = [
            'title',
            'description',
        ]