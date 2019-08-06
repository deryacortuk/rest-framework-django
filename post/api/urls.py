
from django.urls import path
from .views import PostListApiView,PostDetailAPIView,PostUpdateAPIView,PostCreateAPIView
from django.views.decorators.cache import cache_page
app_name = "post"

urlpatterns = [
    path('list',cache_page(60*1)(PostListApiView.as_view()),name="list"),
    path('list',PostListApiView.as_view(),name="list"),
    path('detail/<slug>',PostDetailAPIView.as_view(), name="detail"),

    path('update/<slug>',PostUpdateAPIView.as_view(), name="update"),
    path('create/',PostCreateAPIView.as_view(), name="update"),

]
