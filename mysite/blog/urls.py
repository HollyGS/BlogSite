from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]
