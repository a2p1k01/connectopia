from django.shortcuts import render, redirect

from chat.forms import ChatMessageForm
from chat.models import ChatMessage


def chat(request):
    messages = ChatMessage.objects.all()
    message_form = ChatMessageForm(data=request.POST)
    if request.method == 'POST':
        if 'send-message' in request.POST and message_form.is_valid():
            message = message_form.save(commit=False)
            message.user = request.user
            message.save()
        elif 'delete-message' in request.POST:
            message = messages.filter(id=int(request.POST.get('delete-message', 1)))
            message.delete()
        return redirect('/chat')
    return render(request, 'chat.html',
                  {'messages': messages, 'message_form': message_form, 'user': request.user}
                  )
