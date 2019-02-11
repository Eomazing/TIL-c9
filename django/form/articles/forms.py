from django import forms
from .models import Article # 두번째 class 작성 시 추가


class ArticleForm(forms.Form): # 상속받는 자식 class
    title = forms.CharField(label='제목') # forms에서 가지고 왔기 때문에 max_length 필수 아님.
    content = forms.CharField(label='내용', widget=forms.Textarea(attrs={
        'row':5,
        'cols':50,
        'placeholder': '내용을 입력하세요.',
    }))
    
class ArticleModelForm(forms.ModelForm): # django forms에서 ModelsForm 상속받음.
    class Meta: # 이름 꼭 지켜줘야함!! class의 정보가 담기는 역할.
        # Meta : 데이터를 설명하는 데이터.
        model = Article
        fields = ['title', 'content']
        