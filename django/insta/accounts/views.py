from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
# 회원가입 만들기
def signup(request):
    # 로그인이 되어있다면, list페이지로 redirect
    if request.user.is_authenticated:
        return redirect('posts:list')
    if request.method == 'POST':
        # user 정보를 가지고 와서 signup_form에 담는다.
        signup_form = UserCreationForm(request.POST)
        # 중복되지 않고, 유효한 user 정보가 들어 왔다면,
        if signup_form.is_valid():
            user = signup_form.save()
            auth_login(request, user)
            # 우선적으로 list로 돌려보낸다.(아직 회원정보 페이지 등이 만들어지지 않았음)
            return redirect('posts:list')
    else:
        # GET 요청이 들어왔을 경우, 수정되는 내용
        signup_form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'signup_form':signup_form})


def login(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
        
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        # 실제 존재하는 user라면 유효한 값.
        if login_form.is_valid():
            # 첫번째로 parameter(request) 입력하고, user 객체 순으로 들어온다.
            auth_login(request, login_form.get_user())
            return redirect(request.GET.get('next') or 'posts:list')
    else:
        login_form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'login_form':login_form})
    
def logout(request):
    auth_logout(request)
    # 로그아웃은 따로 페이지가 필요없으므로 redirect
    return redirect('posts:list')