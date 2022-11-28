from django import forms
from authen.models import Content
from forum.models import Forum
import re

class TaskForms(forms.ModelForm):
    name_list = list(Forum.objects.values_list('title'))
    pk_list = list(Forum.objects.values_list('pk'))
    temp = []
    for i in range(len(name_list)):
        temp.append(tuple([pk_list[i][0], name_list[i][0]]))
    forum_option = tuple(temp)
    group = forms.MultipleChoiceField(choices=forum_option)
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
        
        regex = "^[A-Za-z0-9._~-]*$"
        if not (bool(re.match(regex, title))):
            raise forms.ValidationError("Nama tidak valid")
        
        return title
        
        