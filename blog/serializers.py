from rest_framework.serializers import ModelSerializer
from .models import Post, Notice

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
class NoticeSerializer(ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'