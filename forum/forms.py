from django import forms
from authen.models import Content
from forum.models import Forum
import re

class TaskForms(forms.ModelForm):
    class Meta:
        model = Content
        fields = [
            'title',
            'description',
        ]

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = [
            'title',
            'description',
        ]
    
    def clean_title(self):
        data = self.cleaned_data
        if not ('title' in data.keys()):
            raise forms.ValidationError(("Please fill out missing fields."))

        title = data['title']
        
        regex = "^[A-Za-z0-9-]*$"
        if not (bool(re.match(regex, title))):
            raise forms.ValidationError("Nama tidak valid")
        
        return title
        
        