from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    notification_count = serializers.ReadOnlyField()



    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    

    class Meta:
        model = Notification
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title',
            'content', 'is_owner', 'notification_count'
        ]