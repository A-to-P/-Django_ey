from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import TextInput
from .models import User

class UserLoginForm(AuthenticationForm):
    pass

class UserSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 사용할 모델 명시 필수
        model = User

        fields = [
            'username'
        ]

        widgets = [
            'username'
        ]