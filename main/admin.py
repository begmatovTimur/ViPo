from django.contrib import admin
from main.models import Post, Tag, User, Comment

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(User)
admin.site.register(Comment)