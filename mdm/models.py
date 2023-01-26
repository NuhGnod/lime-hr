from django.db import models

# Create your models here.
# class EvalItem(models.Model):
#     eval_item_no = models.AutoField(primary_key=True)
#     eval_item_clss = models.CharField(max_length=10, blank=True, null=True)
#     item_nm = models.CharField(max_length=100, blank=True, null=True)
#     item_desc = models.CharField(max_length=200, blank=True, null=True)
#     reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
#     modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
#     reg_mem_no = models.IntegerField(blank=True, null=True)
#     modf_mem_no = models.IntegerField(blank=True, null=True)
#     del_yn = models.CharField(max_length=1, default='N', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'eval_item'
#
