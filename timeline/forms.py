import imp
from django import forms
from authen.models import Content
from forum.models import Forum
from timeline.models import Comment

class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comment'
        ]
