from django import forms
from .models import Comment, Profile, Suport
from django.contrib.auth.models import User


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


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'email'}


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')


class SuportForm(forms.ModelForm):
    class Meta:
        model = Suport
        fields = {'name', 'email', 'phone', 'body'}