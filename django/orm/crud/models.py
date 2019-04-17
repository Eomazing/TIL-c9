from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField()
    
# 용어 정리
# class Post : Django - Model, DB - Table
# post = Post() : Django - Instance or Object, DB - Record or Row
# title : Django - Field, DB - Column

# CRUD
# 1. Create
# 1. 방법 1
# post = Post(title='hello-1')
# post.save()

# 2. 방법 2
# post2 = Post.objects.create(title='hello-2')

# 2. 방법 2
# post3 = Post()
# post3.title = 'hello-3'
# post3.save()

# 2. Read
# 2-1. All
# posts = Post.objects.all()

# 2-2. One
# 방법 1
# post = Post.objects.get(pk=1) # id=1, title='hello-1'도 가능

# 방법 2 (views.py 한정)
# from django.shortcuts import get_object_or_404
# post = get_object_or_404(Post, pk=1) # id=1, title='hello-1'도 가능

# 방법 3
# post = Post.objects.filter(pk=1)[0] # id=1, title='hello-1'도 가능
# post = Post.objects.filter(pk=1).first()

# 2-3. Where(filter)
# posts = Post.objects.filter(title='hello-1') # 명확하게 title='hello-1' => if not, error 발생
# post = Post.objects filter(title='hello-1').first() # 또는 [0]

# LIKE
# posts = Post.objects.filter(title__contains='lo')

# order_by
# posts = Post.objects.order_by('title') # 제목 오름차순
# posts = Post.objects.order_by('-title') # 제목 내림차순

# offset & limit
# Post.objects.all()[0] #=> offset 0 limit 1
# Post.objects.all()[1] #=> offset 1 limit 1
# Post.objects.all()[1:3] #=> offset 1 limit 2
# Post.objects.all()[offset:offset+limit]

# 3. Update
# post = Post.objects.get(pk=1)
# post.title = 'hello-5'
# post.save() # 실제 데이터베이스에 저장

# 4. Delete
# post = Post.objects.get(pk=1)
# post.delete()
# 한줄로
# Post.objects.get(pk=1).delete()