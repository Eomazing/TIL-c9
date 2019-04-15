from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model # 현재 사용하고 있는 Form의 model도 가지고 와야한다.

# UserChangeForm을 가지고 새로운 class를 만들겠다.
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name',]