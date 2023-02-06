from django.db import models
from accounts.models import EusoMem


# Create your models here.
class CommCd(models.Model):
    comm_cd = models.CharField(primary_key=True, max_length=10)
    hi_comm_cd = models.CharField(max_length=10, blank=True, null=True)
    cd_nm = models.CharField(max_length=100)
    cd_desc = models.CharField(max_length=200, blank=True, null=True)
    etc_1 = models.CharField(max_length=100, blank=True, null=True)
    etc_2 = models.CharField(max_length=100, blank=True, null=True)
    etc_3 = models.CharField(max_length=100, blank=True, null=True)
    alias_cd = models.CharField(max_length=10, blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    del_yn = models.CharField(max_length=1, default="N", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comm_cd'


class ZipCd(models.Model):
    zip_no = models.CharField(primary_key=True, max_length=6)
    sido = models.CharField(max_length=20, blank=True, null=True)
    sigungu = models.CharField(max_length=20, blank=True, null=True)
    eupmyun = models.IntegerField(blank=True, null=True)
    doro_cd = models.IntegerField(blank=True, null=True)
    doro_nm = models.CharField(max_length=80, blank=True, null=True)
    build_no1 = models.IntegerField(blank=True, null=True)
    build_no2 = models.IntegerField(blank=True, null=True)
    build_nm = models.CharField(max_length=200, blank=True, null=True)
    dong_cd = models.CharField(max_length=10, blank=True, null=True)
    dong_nm = models.CharField(max_length=20, blank=True, null=True)
    ri = models.CharField(max_length=20, blank=True, null=True)
    h_dong_nm = models.CharField(max_length=20, blank=True, null=True)
    zibun1 = models.IntegerField(blank=True, null=True)
    zibun2 = models.IntegerField(blank=True, null=True)
    zip_no_old = models.CharField(max_length=6, blank=True, null=True)
    zip_sn = models.CharField(max_length=3, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True)
    modf_dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'zip_cd'


class CsOrgn(models.Model):
    cs_no = models.AutoField(primary_key=True)
    zip_no = models.ForeignKey('ZipCd', models.DO_NOTHING, blank=True, null=True, db_column='zip_no')
    cs_nm = models.CharField(max_length=100, blank=True, null=True)
    orgn_reg_no = models.CharField(max_length=13, blank=True, null=True)
    busir_no = models.CharField(max_length=10, blank=True, null=True)
    tel_no = models.CharField(max_length=12, blank=True, null=True)
    fax_no = models.CharField(max_length=12, blank=True, null=True)
    cs_addr = models.CharField(max_length=100, blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    del_yn = models.CharField(max_length=1, default="N", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cs_orgn'


class EusoPjt(models.Model):
    pjt_no = models.AutoField(primary_key=True)
    cs_no = models.ForeignKey(CsOrgn, models.DO_NOTHING, db_column='cs_no')
    pjt_nm = models.CharField(max_length=100, blank=True, null=True)
    start_dt = models.DateField(max_length=8, blank=True, null=True)
    end_dt = models.DateField(max_length=8, blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    del_yn = models.CharField(max_length=1, default="N", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'euso_pjt'


class PjtJoinHist(models.Model):
    join_hist_no = models.AutoField(primary_key=True)
    pjt_no = models.ForeignKey(EusoPjt, models.DO_NOTHING, db_column='pjt_no')
    mem_no = models.ForeignKey(EusoMem, models.DO_NOTHING, db_column='mem_no')
    role_cd = models.CharField(max_length=10, blank=True, null=True)
    enter_dt = models.DateField(max_length=8, blank=True, null=True)
    out_dt = models.DateField(max_length=8, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, default='N', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pjt_join_hist'


class EusoDept(models.Model):
    dept_no = models.AutoField(primary_key=True)
    dept_cd = models.CharField(max_length=10, blank=True, null=True)
    dept_nm = models.CharField(max_length=50, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)
    hi_dept_no = models.IntegerField(blank=True, null=True)

    def __str__(self):
        if self.hi_dept_no:
            hi_dept_nm = EusoDept.objects.get(dept_no=self.hi_dept_no).dept_nm
            dept_group_nm = CommCd.objects.get(comm_cd=self.dept_cd)

        return "(" + hi_dept_nm + " / " + dept_group_nm + ")" + self.name

    class Meta:
        managed = True
        db_table = 'euso_dept'
