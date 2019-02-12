from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:list')
    else:
        form = UserCreationForm()
        
    return render(request, 'signup.html', {'form': form})
    
# Session Create    
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user()) 
            # 실제 로그인 정보가 저장되는 auth_login
            # form.get_user()데이터에 해당하는 User를 가져만 오는 역할.
            return redirect('posts:list')
    else:
        form = AuthenticationForm() # User가 존재하는지 검증하는 역할.
    
    request.GET.get('next')
    return render(request, 'login.html', {'form': form})
    
# Session Delete
def logout(request):
    auth_logout(request)
    return redirect('posts:list')
    