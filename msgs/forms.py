from django.forms import ModelForm, Textarea, TextInput
from .models import Message
from datetime import datetime

class MessageForm(ModelForm):

    class Meta:
        model = Message
        fields = {'value'}
        widgets = {
            'value': Textarea(),
            #'user': TextInput(),
        }

    # def save(self, commit=True):
    #     user = super(MessageForm, self).save(commit=False)
    #     user.value = self.cleaned_data['value']
    #     user.date = datetime.now()
    #     if commit:
    #         user.save()
    #     else:
    #         return user

