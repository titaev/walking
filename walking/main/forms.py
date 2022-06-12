from .models import Rewiew
from django import forms

class RewiewForm(forms.ModelForm):


    class Meta:
        model = Rewiew
        fields = ('rating', 'description')

