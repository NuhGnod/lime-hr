from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, Group
)


class MemberManager(BaseUserManager):
    def create_user(self, username, password, name):
        member = self.model(
            name=name,
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
            username=username,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class EusoMem(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(db_column='id', primary_key=True, verbose_name='아이디')
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True, null=False, verbose_name='이메일')
    name = models.CharField(max_length=50)
    is_superuser = models.IntegerField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    posi_cd = models.CharField(max_length=10, blank=True, null=True)
    duty_resp_cd = models.CharField(max_length=10, blank=True, null=True)
    dept_no = models.IntegerField(db_column='dept_no', blank=True, null=True)
    zip_no = models.CharField(max_length=50,blank=True, null=True)
    mem_addr = models.CharField(max_length=100, blank=True, null=True)
    join_dt = models.CharField(max_length=8, blank=True, null=True)
    mem_stat_cd = models.CharField(max_length=10, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True, default='N')

    objects = MemberManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', ]
    class Meta:
        managed = True
        db_table = 'euso_mem'
        ordering = ['-join_dt']