from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    link_pk = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = Comment
        fields = ('body',)
        forms.widgets = {
            'body': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }
        