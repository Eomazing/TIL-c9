from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# 추가적인 저장 공간
def post_image_path(instance, filename): # instantce:받는 정보, 파일이름(upload 하는)
    return f'posts/images/{filename}'
    # return 'posts/{}/{}'.format(instantce.content, filename) # 경로값/파일이름
            # 업로드 하면서 파일 이름을 변경하고 싶다면, 아래의 방법 참고
            # (파일 이름에 사용할 수 없는 문자가 들어온다면 위험할 수 있음)
    # return 'posts/{}/{}'.format(instantce.content, instantce.content.jpg)
    
# Create your models here.
class Post(models.Model):
    content = models.TextField()
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(
            upload_to=post_image_path, # 저장 위치 => 함수 호출
            processors=[ResizeToFill(600,600)], # 처리할 작업 목록
            format='JPEG', # 저장 포맷
            options={'quality':90}, # 옵션
        )