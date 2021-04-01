from django.shortcuts import render
from rest_framework.decorators import api_view
from api.models import Post
from api.serializers import PostSerializer, GetUuidPostSerializer, GetContentPostSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def post_blog(request):
    if request.method == 'POST':
        post_data = JSONParser().parse(request)
        post_serializer = PostSerializer(data=post_data)
        print(post_serializer)
        if post_serializer.is_valid():
            post_obj = post_serializer.save()
            obj_uuid = GetUuidPostSerializer(post_obj).data['postuuid']
            response_data = {
                'uuid':obj_uuid
            }
            return JsonResponse(response_data, status=status.HTTP_201_CREATED) 
        return JsonResponse({'message': 'The Post could not be created'}, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['GET', 'PUT', 'DELETE'])
def edit_blog(request):
    post_data = JSONParser().parse(request)
    obj_uuid = GetUuidPostSerializer(data = post_data).initial_data['postuuid']
    print(obj_uuid)
    try: 
        post = Post.objects.get(pk=obj_uuid) 
    except Post.DoesNotExist: 
        return JsonResponse({'message': 'The Post does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        post_serializer = PostSerializer(post) 
        print(post_serializer.data)
        return JsonResponse(post_serializer.data)
 
    elif request.method == 'PUT': 
        print(post_data['content'])
        post.content =  post_data['content']
        post.save()
        return JsonResponse({'message' : 'The post successfully updated'})
 
    elif request.method == 'DELETE': 
        post.delete() 
        return JsonResponse({'message': 'Post was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)