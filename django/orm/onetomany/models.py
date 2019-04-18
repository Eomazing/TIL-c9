from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField()

# User:Post = 1:N
class Post(models.Model):
    title = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# User:Comment = 1:N
# Post:Comment = 1:N
class Comment(models.Model): # N의 class에 1에 해당하는 정보를 기록해야 한다.
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 1에 해당하는 정보
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # 1에 해당하는 정보
    
# 예시
# 1. 1번 사람이 작성한 게시글은?
# user1.post_set.all()

# 2. 1번 사람이 작성한 게시글의 댓글들을 출력.
# for post in user1.post_set.all():
#   for comment in post.comment_set.all():
#       print(comment.content)

# 3. 2번 댓글을 쓴 사람은?
# c2.user

# 4. 2번 댓글을 쓴 사람이 작성한 게시글은?
# c2.user.post_set.all()

# 5. 1번 글의 첫번째 댓글을 쓴 사람의 이름은?
# post1.comment_set.first().user.name

# 6. '1'글이라는 제목인 게시글은?
# Post.objects.filter(title='1글')

# 7. 댓글 중에 해당 게시글의 제목이 1글인 것은?
# 방법 1
# Comment.objects.filter(post__title='1글')
# 방법 2
# post1 = Post.objects.get(title='1글')
# Comment.objects.filter(post=post1)

# 8. 댓글 중에 해당 게시글의 제목에 '1'이 들어가 있는 것은?
# Comment.objects.filter(post__title__contains='1')
