from django import forms
from .models import Link

class LinkForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    url = forms.URLField(widget=forms.URLInput(attrs={'class':'form-control'}))
    class Meta:
        model = Link
        fields = ('title','url')

   