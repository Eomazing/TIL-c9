from django.contrib import admin
from .models import Post, Comment

# PostAdmin class 만들기
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content', 'created_at', 'updated_at',)

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)