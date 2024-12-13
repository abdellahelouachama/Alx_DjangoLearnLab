from rest_framework import viewsets
from .serializers import CommentSerializer, PostSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from .models import Comment, Post
from rest_framework.decorators import action
from .permissions import IsOwner
from rest_framework.filters import SearchFilter
from django.contrib.auth import get_user_model
User = get_user_model()

# post viewset to preform crud operations for the post it required authentication 
# and the the authenticated user to be the auther of the bost for object level actions
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'content']
    search_fields = ['title', 'content']

    def get_object(self):
        
        """
        Retrieve and return the post object based on the lookup field.

        Checks the permissions for the retrieved object before returning it.

        Returns:
            Post: The post object if permissions are granted and the object is found.
        """
        
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj
    
    def create(self, request, *args, **kwargs):
        """
    Handle the creation of a new post.

    Args:
        request (Request): The request object containing post data, including title and content.

    Returns:
        Response: A response indicating the success or failure of the post creation.
                  On success, returns a message with HTTP 201 status. On failure,
                  returns error details with HTTP 400 status.
        """
        user = User.objects.get(username=request.user)
        author = user.id
        title = request.data.get('title')
        content = request.data.get('content')
        
        post_data = {'author':author, 'title':title, 'content':content}
        serializer = PostSerializer(data=post_data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Post creation successful'}, status=status.HTTP_201_CREATED)
        
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['GET'], detail=False, url_path='feed')
    def feed(self, request):
        """
        Retrieve and return posts from users that the authenticated user follows.

        Returns a list of posts authored by users that the authenticated user follows.
        If no posts are found, returns a message indicating no posts are available.

        Args:
            request (Request): The request object containing user authentication information.

            Returns:
            Response: A response with serialized post data and HTTP 200 status if posts exist,
              otherwise a message with HTTP 204 status indicating no posts found.
        """
        followed_users = request.user.following.all()
        posts = self.queryset.filter(author__in=followed_users)
        
        if posts.exists():
             serializer = PostSerializer(instance=posts, many=True)
             return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({'message': 'No posts found'}, status=status.HTTP_204_NO_CONTENT)


# comment viewset to preform crud operations for the post it required authentication and 
# the the authenticated user to be the auther od comment for object level actions
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self):
        """
    Retrieve and return the comment object based on the lookup field.

    Checks the permissions for the retrieved object before returning it.

    Returns:
        Comment: The comment object if permissions are granted and the object is found.
        """
        obj =  super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj
    
    def create(self, request, *args, **kwargs):
        """
    Handle the creation of a new comment.

    Args:
        request (Request): The request object containing comment data, including title and content.

    Returns:
        Response: A response indicating the success or failure of the comment creation.
                  On success, returns a message with HTTP 201 status. On failure,
                  returns error details with HTTP 400 status.
        """
        author = request.user
        title = request.data.get('title')
        content = request.data.get('content')
        post = request.data.get('post')
        
        comment_data = {'author':author.id, 'title':title, 'content':content, 'post':post}
        serializer = CommentSerializer(data=comment_data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Comment creation successful'}, status=status.HTTP_201_CREATED)
        
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

