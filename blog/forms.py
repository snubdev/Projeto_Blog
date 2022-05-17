from django import forms


class EmailPostForm(forms.Form):
    nome = forms.CharField(max_length=25)
    email = forms.EmailField()
    para = forms.EmailField()
    comentarios = forms.CharField(required=False, widget=forms.Textarea)

