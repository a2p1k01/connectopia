from django import forms

from post.models import Post, Comment


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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update({'class': 'p-2 bg-slate-100 border rounded border-slate-500 w-full'})

