from django.contrib import admin
from .models import Post

# PostAdmin class 만들기
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content')

# Register your models here.
admin.site.register(Post, PostAdmin)