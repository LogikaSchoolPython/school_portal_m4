from django.contrib import admin
from .models import UserProfile, Role, Post, Comment, Article

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Role)
admin.site.register(Article)
