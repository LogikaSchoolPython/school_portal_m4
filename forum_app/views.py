from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Comment, Article
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    PermissionRequiredMixin,
)
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CommentForm


class PostListView(ListView):
    model = Post
    template_name = "forum_app/posts.html"  # ваш шаблон
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "forum_app/post_detail.html"  # ваш шаблон

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()  # Додаємо форму до контексту
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.get_object()
            comment.author = request.user  # або встановіть автора за вашим сценарієм
            comment.save()
            return redirect("post-detail", pk=comment.post.pk)


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "forum_app/post_form.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user  # Встановлюємо автора посту
        return super().form_valid(form)

    def test_func(self):
        return (
            self.request.user.userprofile.role.name == "Moderator"
            or self.request.user.userprofile.role.name == "Administrator"
        )


class ArticleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Article
    fields = ["title", "content"]
    template_name = "forum_app/article_form.html"
    permission_required = "forum_app.can_publish"
    success_url = reverse_lazy("home")


def custom_403_view(request, exception=None):
    return render(
        request, "403.html", {"message": "Особливе повідомлення!"}, status=403
    )
