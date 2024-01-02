from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from post.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image', 'tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'p-2 bg-slate-100 border rounded border-slate-500 w-full'})
        self.fields['body'].widget.attrs.update({'class': 'p-2 bg-slate-100 border rounded border-slate-500 w-full'})
        self.fields['image'].widget.attrs.update({'class': 'p-2 bg-slate-100 border rounded border-slate-500 w-full'})
        self.fields['tags'].widget.attrs.update({'class': 'p-2 bg-slate-100 border rounded border-slate-500 w-full'})


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'p-2 bg-slate-100 border rounded border-slate-500 w-full'}
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'p-2 bg-slate-100 border rounded border-slate-500 w-full'}
        )
        self.fields['password1'].widget.attrs.update(
            {'class': 'p-2 bg-slate-100 border rounded border-slate-500 w-full'}
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'p-2 bg-slate-100 border rounded border-slate-500 w-full'}
        )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'p-2 bg-slate-100 border rounded border-slate-500 w-full'})
        self.fields['password'].widget.attrs.update({'class': 'p-2 bg-slate-100 border rounded border-slate-500 w-full'})
