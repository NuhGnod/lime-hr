from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, Group
)


class MemberManager(BaseUserManager):
    def create_user(self, username, password, name):
        member = self.model(
            name=name,
            password='dbzmfflem1!',
            email=self.normalize_email(username),
            username=username,
        )

        member.set_password(password)
        member.save(using=self._db)
        return member

    def create_superuser(self, username, password, name):
        user = self.create_user(
            password=password,
            name=name,
            email=username,
            username=username,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def save(self, *args, **kwargs):
        print("=====")
        print("저장")
        print("=====")
        user = super().save(commit=False)
        if self.cleaned_data["password"] is None:
            user.set_password('dbzmfflem1!')
        else:
            user.set_password(self.cleaned_data["password"])

        user.save()
        return user


class EusoMem(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(db_column='id', primary_key=True, verbose_name='아이디')
    username = models.CharField(max_length=150, unique=True, blank=True, null=True, verbose_name="로그인ID")
    password = models.CharField(max_length=128, blank=True, null=True, verbose_name="비밀번호")
    email = models.EmailField(max_length=50, unique=True, null=False, verbose_name='이메일')
    name = models.CharField(max_length=50, verbose_name="사원명")
    is_superuser = models.BooleanField(default=False, verbose_name="시스템관리자 여부")
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)
    posi_cd = models.CharField(max_length=20, blank=True, null=True)
    duty_resp_cd = models.CharField(max_length=20, blank=True, null=True)
    dept_no = models.IntegerField(db_column='dept_no', blank=True, null=True)
    zip_no = models.CharField(max_length=50, blank=True, null=True)
    mem_addr = models.CharField(max_length=100, blank=True, null=True)
    join_dt = models.CharField(max_length=8, blank=True, null=True)
    mem_stat_cd = models.CharField(max_length=20, blank=True, null=True, verbose_name="회원상태코드")
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True, default='N', verbose_name="삭제여부")
    is_staff = models.BooleanField(default=False, verbose_name="시스템관리자 여부")
    objects = MemberManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', ]

    class Meta:
        managed = False
        db_table = 'euso_mem'
        ordering = ['-join_dt']
