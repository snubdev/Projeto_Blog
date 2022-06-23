from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    nome = forms.CharField(max_length=25)
    email = forms.EmailField()
    para = forms.EmailField()
    comentarios = forms.CharField(required=False, widget=forms.Textarea)


# Formulário de comentarios
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'name', 'email', 'body'}


class SearchForm(forms.Form):
    query = forms.CharField


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
