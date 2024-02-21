from rest_framework import serializers
from .models import Draft

# Serializing our posts resource so the api can be able to
# post and get data in the required form.


class DraftSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
   

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
            

    class Meta:
        model = Draft
        fields = [
            'id', 'owner', 'is_owner', 'created_at', 'updated_at',
            'title', 'content', 'image',
        ]