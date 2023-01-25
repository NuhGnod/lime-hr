from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, Group
)


class MemberManager(BaseUserManager):
    def create_user(self, username, password, email, name, blng_orgn_nm, blng_orgn_cd):
        member = self.model(
            name=name,
            email=self.normalize_email(email),
            username=username,
            # blng_orgn_nm=blng_orgn_nm,
            # blng_orgn_cd=blng_orgn_cd
        )

        member.set_password(password)
        member.save(using=self._db)
        return member

    def create_superuser(self, email, password, name):
        user = self.create_user(
            password=password,
            name=name,
            email=self.normalize_email(email)
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class EusoMem(AbstractBaseUser, PermissionsMixin):

    id = models.AutoField(db_column='id', primary_key=True, verbose_name='아이디')
    username = models.CharField(max_length=150, null=False, unique=True, verbose_name='로그인아이디')
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=50, unique=True, null=False, verbose_name='이메일')
    name = models.CharField(max_length=20, null=False, verbose_name='이름')
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField(blank=True, null=True)

    posi_cd = models.CharField(max_length=10, blank=True, null=True)
    duty_resp_cd = models.CharField(max_length=10, blank=True, null=True)
    dept_no = models.IntegerField( db_column='dept_no')
    zip_no = models.CharField(max_length=10, blank=True, null=True, db_column='zip_no')
    mem_addr = models.CharField(max_length=200, blank=True, null=True)
    join_dt = models.CharField(max_length=8, blank=True, null=True)
    mem_stat_cd = models.CharField(max_length=10, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField()
    modf_dt = models.DateTimeField(blank=True, null=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    objects = MemberManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', ]
    class Meta:
        managed = False
        db_table = 'euso_mem'
        ordering = ['-join_dt']