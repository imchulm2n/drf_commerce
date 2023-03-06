from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserManager(BaseUserManager):
    """
    유저 생성 헬퍼클래스 (일반 유저, 관리자)
    """
    # 일반 user 생성
    def create_user(self, email, username, name, password=None):
        if not email:
            raise ValueError('must have user email')
        if not username:
            raise ValueError('must have user username')
        if not name:
            raise ValueError('must have user name')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            name = name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # 관리자 user 생성
    def create_superuser(self, email, username, name, password=None):
        user = self.create_user(
            email,
            password = password,
            username = username,
            name = name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    GENDER_CHOICES = (('Male', '남성'), ('Female', '여성'))

    username = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False
        )
    email = models.EmailField(
        max_length=30, 
        unique=True, 
        null=False, 
        blank=False
        )
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False
        )
    city = models.CharField(
        max_length=100, 
        null=False,
        blank=False
        )
    birth_date = models.DateField(
        verbose_name=_('Birth Date'),
        null=False,
        )
    gender = models.CharField(
        max_length=6, 
        choices=GENDER_CHOICES, 
        null=False, 
        blank=False
        )
    zipcode = models.CharField(
        max_length=20, 
        null=True, 
        blank=True
        )

    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)
    
    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 username으로 설정
    USERNAME_FIELD = 'username'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['email', 'name', 'birth_date', 'gender']

    def __str__(self):
        return self.username
