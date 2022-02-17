from django.shortcuts import get_object_or_404, render, redirect
from .forms import MessageForm
from .models import Message
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime

# Create your views here.
def send(request, username):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        a7a = False
        if form.is_valid():
            value = form.cleaned_data.get('value')
            user = User.objects.get(username=username)
            date = datetime.now()
            positive = ['lov', 'positiv', 'thank', 'appreciat', 'beaut', 'pretty',
                        'handsome', 'happ', 'welcom', 'good', 'delight', 'ador', 'kind',
                        'attractive', ''
                        'حب', 'دعم', 'شكر', 'تقدير', 'قدر', 'جميل', 'أنيق',
                        'أناقة', 'وسيم', 'وسامة', 'سعيد', 'سعاد', 'خير', 'عشق', 'طيب',
                        'جذاب', 'يسر', 'سرور', 'لطف', ''
                        ]
            for word in positive:
                if word in value:
                    a7a = True
                    return render(request, 'msgs/send.html', {'form':form, 'a7a':a7a})
                else:
                    a7a = False
            try:
                msg = Message(value=value, user=user, date=date)
                msg.save()
                return redirect('logreg:index')
            except:
                messages.error(request, 'User not found!')
    else:
        form = MessageForm()
    return render(request, 'msgs/send.html', {'form':form})

def my_msgs(request):
    if request.user.is_authenticated:
        username = request.user.id
        try:
            msgs = Message.objects.filter(user = username) 
        except Message.DoesNotExist:
            msgs = None
    else:
        msgs = None
    return render(request, 'msgs/my_msgs.html', {'msgs':msgs})

def fav(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    message.fav = not message.fav
    message.save()
    return redirect('msgs:my_msgs')
