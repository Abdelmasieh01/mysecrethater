from django.contrib import admin
from .models import Message

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('value', 'date', 'fav')
        },),
        ('Sent to', {
            'fields': ('user',)
        },),
    )

admin.site.register(Message, MessageAdmin)