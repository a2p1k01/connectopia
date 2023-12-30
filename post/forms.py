from django import forms

from post.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'bg-slate-100 border rounded border-slate-500 w-full'})
        self.fields['body'].widget.attrs.update({'class': 'bg-slate-100 border rounded border-slate-500 w-full'})
