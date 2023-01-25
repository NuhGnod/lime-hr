from django.db import models

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
    reg_dt = models.DateTimeField()
    modf_dt = models.DateTimeField()
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comm_cd'