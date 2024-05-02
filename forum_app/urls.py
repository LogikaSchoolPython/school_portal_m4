from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    ArticleCreateView,
    custom_403_view,
)
from django.contrib.auth import views as auth_views
from django.conf.urls import handler403

handler403 = custom_403_view

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="new-post"),
    path("article/new/", ArticleCreateView.as_view(), name="new-article"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="forum_app/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
