from socket import fromshare
from django import forms
from hall_of_shame.models import Corruptor

class CorruptorForm(forms.ModelForm):
    class Meta:
        model = Corruptor
        fields = ['name', 'arrested_date', 'corruption_type', 'description']
