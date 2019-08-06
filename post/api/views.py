
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateAPIView
from post.models import Post
from post.api.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from rest_framework.filters import  SearchFilter,OrderingFilter
from post.api.paginations import PostPagination
from rest_framework.mixins import CreateModelMixin, ListModelMixin,DestroyModelMixin


class PostListApiView(ListAPIView,CreateModelMixin):

    serializer_class = PostSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields=['title','content']
    pagination_class = PostPagination


    def get_queryset(self):
        queryset=Post.objects.filter(draft=False)
        return queryset
    def post(self , request,*args ,**kwargs):
        return self.create( request,*args ,**kwargs)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'





class PostUpdateAPIView(RetrieveUpdateAPIView, DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)
    def delete(self, request,*args ,**kwargs):
        return self.destroy( request,*args ,**kwargs)

class PostCreateAPIView(CreateAPIView, ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    def get(self,request,*args ,**kwargs):
        return self.list( request,*args ,**kwargs)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)



