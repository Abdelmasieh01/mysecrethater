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
        if form.is_valid():
            value = form.cleaned_data.get('value')
            user = User.objects.get(username=username)
            date = datetime.now()
            if reject_positive(value):
                reject = True
                return render(request, 'msgs/send.html', {'form': form, 'reject': reject})
            try:
                msg = Message(value=value, user=user, date=date)
                msg.save()
                return redirect('logreg:index')
            except:
                messages.error(request, 'User not found!')
    else:
        form = MessageForm()
    reject = False
    return render(request, 'msgs/send.html', {'form': form, 'reject': reject})


def my_msgs(request):
    if request.user.is_authenticated:
        username = request.user.id
        try:
            msgs = Message.objects.filter(user=username).order_by('-date')
        except Message.DoesNotExist:
            msgs = None
    else:
        msgs = None
    return render(request, 'msgs/my_msgs.html', {'msgs': msgs})


def fav(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    message.fav = not message.fav
    message.save()
    return redirect('msgs:my_msgs')

def reject_positive(value):
    positive = ['lov', 'positiv', 'thank', 'appreciat', 'beaut', 'pretty',
                'handsome', 'happ', 'welcom', 'good', 'delight', 'ador', 'kind',
                'attractive',
                'حب', 'دعم', 'شكر', 'تقدير', 'قدر', 'جميل', 'أنيق',
                'أناقة', 'وسيم', 'وسامة', 'سعيد', 'سعاد', 'خير', 'عشق', 'طيب',
                'جذاب', 'يسر', 'سرور', 'لطف',
                ]
    for word in positive:
        if word in value:
            return True
        else:
            continue
    return False
