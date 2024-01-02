from django import forms

from chat.models import ChatMessage


class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update(
            {'class': 'p-2 bg-slate-100 border h-15 rounded-xl border-slate-500',
             'style': 'width: 56rem;'}
        )
