from msgs.models import Message
from rest_framework import serializers

class messageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'