from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# ORM실행시 호출되는 매써드를 관리
class UserManager(BaseUserManager):
    
    # superuser
    # password는 AbstractBaseUser에 명시, **kwargs는 여러개의 인자를 딕셔너리로 받아줌
    def create_superuser(self, username, password **kwargs):
        user = self.model(
            username = username
        )
        # 암호화 위해 user.password = password 대신 set_password 사용
        user.set_password(password)
        user.save()

class User(AbstractBaseUser, PermissionsMixin):
    # 로그인시 뭐로 인증할 지 명시
    USERNAME_FIELD = 'username'

    username = models.CharField(
        unique=True,
        max_length=20,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    @property
    def is_staff(self):
        # 슈퍼 유저인지 아닌지 반환하는 매써드
        return self.is_superuser