# translator for model to json
# Create, Read, Update, Delete
from rest_framework.serializers import Serializer, ModelSerializer

from message.models import Chat_room


class Chat_roomSerializer(ModelSerializer):
    class Meta:
        model = Chat_room
        fields = '__all__'

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Chat_room
        fields = '__all__'


