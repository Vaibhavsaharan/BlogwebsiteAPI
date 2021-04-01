from rest_framework import serializers 
from api.models import Post
 
 
class PostSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Post
        fields = ['title','username','published_on','content']
    
    
class GetUuidPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['postuuid']

class GetContentPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['content']