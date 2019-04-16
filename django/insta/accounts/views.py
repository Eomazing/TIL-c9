from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, ProfileForm, CustomUserCreationForm
from .models import Profile

# Create your views here.
# 회원가입 만들기
def signup(request):
    # 로그인이 되어있다면, list페이지로 redirect
    if request.user.is_authenticated:
        return redirect('posts:list')
    if request.method == 'POST':
        # user 정보를 가지고 와서 signup_form에 담는다.
        signup_form = CustomUserCreationForm(request.POST)
        # 중복되지 않고, 유효한 user 정보가 들어 왔다면,
        if signup_form.is_valid():
            user = signup_form.save()
            Profile.objects.create(user=user) # User의 Profile 생성
            auth_login(request, user)
            # 우선적으로 list로 돌려보낸다.(아직 회원정보 페이지 등이 만들어지지 않았음)
            return redirect('posts:list')
    else:
        # GET 요청이 들어왔을 경우, 수정되는 내용
        signup_form = CustomUserCreationForm()
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
    
def people(request, username): # urls.py 참조
                            # method를 이용해 간접적으로 user model을 사용해야 수정이 용이함.
    # get_user_model() => User
    people = get_object_or_404(get_user_model(), username=username)
    return render(request, 'accounts/people.html', {'people':people})
    
# User Edit(회원 정보 수정) = User CRUD 중 U
@login_required
def update(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('people', request.user.username)
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/update.html',{
                                        'user_change_form': user_change_form,  
                                        })

# User Delete(회원 탈퇴) = User CRUD 중 D
@login_required
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('posts:list')
    else:
        return render(request, 'accounts/delete.html')
        
@login_required
def password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            return redirect('people', request.user.username)
    else:
        password_change_form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password.html',{
                                'password_change_form': password_change_form,
                                })
                                
def profile_update(request):
    profile = request.user.profile # user와 1:1로 연결된 profile을 가지고 profile 변수에 담아서 사용한다.
    if request.method == 'POST': # 원하는 정보를 담아서 보내는 행위는 POST 요청
    # () 안의 내용을 담아서 (nickname, intro/ image file/ instance=profile에 담는다는 의미)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('people', request.user.username)
    else: # 주소창으로 주소를 입력하는 GET요청으로 접근한다면, 단순히 정보를 보여주기만 한다.
        profile_form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_update.html',{
                                            'profile_form': profile_form,
                                        })
                                        
def follow(request, user_id):
    # 어떤 사람을 follow 할 것인지
    followee = get_object_or_404(get_user_model(), id=user_id)
    if request.user in followee.followers.all():
        # 2. followee를 unfollw 하기
        followee.followers.remove(request.user)
    else:
        # 1. followee를 follow 하기
        followee.followers.add(request.user)
    return redirect('people', followee.username) # 다시 user 페이지로 갈 수 있도록