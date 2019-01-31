from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit
# ResizeToFill : 300, 300 맞추고 넘치는 부분 잘라냄.
# ResizeToFit : 300, 300 맞추고 남는 부분을 빈 공간으로 둠.

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(
            upload_to='posts/images', # 저장 위치
            processors=[ResizeToFit(300, 300)], # 순차적으로 처리함 = [처리할 작업 목록]
            format='JPEG', # 저장 포맷 (확장자 설정)
            options={'quality':90}, # 저장 포맷 관련 옵션
        )
    # table 만들 때, 기본적으로 추가하는 cols 2개
    created_at = models.DateTimeField(auto_now_add=True) # create 될 때, 딱 한 번 현재 시각
    updated_at = models.DateTimeField(auto_now=True) # 변경될 때마다, 현재 시각
    
    
    def __str__(self):
        return self.title
    
# Post : Comment = 1 : N    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()


    # on_delete 옵션
    # 1. CASCADE : 부모가 삭제되면, 자기 자신도 삭제.
    # 2. PROTECT : 자식이 존재하면, 부모 삭제 불가능.
    # 3. SET_NULL : 부모가 삭제되면, 자식의 부모 정보에 NULL 설정.
    
    
# 1. Create
# post = Post(title='hello', content='world!')
# post.save()

# 2. Read
# 2.1. All
# posts = Post.objects.all()
# 2.2. Get one
# post = Post.objects.get(pk=1)
# 2.3. filter (WHERE)
# posts = Post.objects.filter(title='Hello').all()
# post = Post.objects.filter(title='HEllo').first()
# 2.4. LIKE
# posts = Post.objects.filter(title__contains='He').all()
# 2.5. order_by (정렬)
# posts = Post.objects.order_by('title').all() => 오름차순
# posts = Post.objects.order_by('-title').all() => 내림차순
# 2.6. limit & offset
# [offset:offset+limit]
# posts = Post.objects.all()[1:2]

# 3. Delete
# post = Post.objects.get(pk=2)
# post.delete()

# 4. Update
# posts = Post.objects.get(pk=1)
# post.title = 'Hi'
# post.save()