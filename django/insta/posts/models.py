from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

# 추가적인 저장 공간
def post_image_path(instance, filename): # instantce:받는 정보, 파일이름(upload 하는)
    return f'posts/images/{filename}'
    # return 'posts/{}/{}'.format(instantce.content, filename) # 경로값/파일이름
            # 업로드 하면서 파일 이름을 변경하고 싶다면, 아래의 방법 참고
            # (파일 이름에 사용할 수 없는 문자가 들어온다면 위험할 수 있음)
    # return 'posts/{}/{}'.format(instantce.content, instantce.content.jpg)
    
# Create your models here.
class Post(models.Model):
    # 1:N 관계              # user table의 정보가 담겨있음(1), 1에 담겨있는 정보가 삭제되었을 때 N에 대한 처리법을 결정 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    
    # M:N 관계
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # 1에 해당하는 내용 (N은 Image)
    file = ProcessedImageField(
            upload_to=post_image_path, # 저장 위치 => 함수 호출
            processors=[ResizeToFill(600,600)], # 처리할 작업 목록
            format='JPEG', # 저장 포맷
            options={'quality':90}, # 옵션
        )

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 1에 해당하는 내용 (N은 comment)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField() # 댓글의 내용을 기록
    
    