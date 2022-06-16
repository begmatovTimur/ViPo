from django.contrib import admin
from main.models import Post, Tag, User

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(User)