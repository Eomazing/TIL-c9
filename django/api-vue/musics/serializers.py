from rest_framework import serializers
from .models import Music, Artist, Comment

# 위치를 상위로 변경시켰다. why? MusicSerializer에서 사용하기 위해 미리 정의 되어 있어야 한다.
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','content',]
        
class MusicSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source='artist.name')
    comment_set = CommentSerializer(many=True)
    class Meta:
        model = Music
        fields = ['id','title','artist_name', 'comment_set']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id','name',]
        
class ArtistDetailSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True)
    class Meta:
        model = Artist
        fields = ['id','name','music_set',] # 정해진 이름!