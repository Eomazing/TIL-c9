from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
# Template variable
def dinner(request):
    # 랜덤 뽑기
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    return render(request, 'dinner.html', {'dinner': pick})
    
# Variable routing
def hello(request, name): # 주소로부터 받고 싶은 변수 => name
    return render(request, 'hello.html', {'name': name})
    
# lotto
def lotto(request):
    numbers = range(1,46)
    lottos = random.sample(numbers, 6)
    return render(request, 'lotto.html', {'lottos': lottos})
    
# Form tag
def throw(request):
    return render(request, 'throw.html')
    
def catch(request):
    message = request.GET.get('message') 
    # GET 은 throw.html 의 method get을 의미함 / get은 딕셔너리 함수 get
    return render(request, 'catch.html', {'message':message})
    
# Form 외부러 요청
def naver(request):
    return render(request, 'naver.html')
    
# Bootstrap
def bootstrap(request):
    return render(request, 'bootstrap.html')