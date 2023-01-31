from django.db import models


class EvalItem(models.Model):
    eval_item_no = models.AutoField(primary_key=True)
    eval_item_clss = models.CharField(max_length=10, blank=True, null=True)
    item_nm = models.CharField(max_length=100, blank=True, null=True)
    item_desc = models.CharField(max_length=200, blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    del_yn = models.CharField(max_length=1, default='N', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'eval_item'


class EvalPlan(models.Model):
    eval_plan_no = models.AutoField(primary_key=True)
    eval_sheet_no = models.ForeignKey('EvalSheet', models.DO_NOTHING, db_column='eval_sheet_no')
    eval_clss = models.CharField(max_length=10, blank=True, null=True)
    eval_plan_nm = models.CharField(max_length=100, blank=True, null=True)
    eval_plan_desc = models.CharField(max_length=200, blank=True, null=True)
    eval_strt_dt = models.DateField(max_length=8, blank=True, null=True)
    eval_end_dt = models.DateField(max_length=8, blank=True, null=True)
    sf_eval_wght = models.IntegerField(blank=True, null=True)
    s_eval_wght = models.IntegerField(blank=True, null=True)
    m_eval_wght = models.IntegerField(blank=True, null=True)
    j_eval_wght = models.IntegerField(blank=True, null=True)
    t_eval_wght = models.IntegerField(blank=True, null=True)
    p_eval_wght = models.IntegerField(blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True, default="N")

    class Meta:
        managed = True
        db_table = 'eval_plan'


class EvalSheet(models.Model):
    eval_sheet_no = models.AutoField(primary_key=True)
    eval_clss = models.CharField(max_length=10, blank=True, null=True)
    sheet_nm = models.CharField(max_length=100, blank=True, null=True)
    sheet_desc = models.CharField(max_length=200, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, default='N', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'eval_sheet'


class EvalRel(models.Model):
    eval_rel_no = models.AutoField(primary_key=True)
    eval_trgt_clss = models.CharField(max_length=10, blank=True, null=True)
    eval_mem_no = models.IntegerField(null=False, blank=False, db_column='eval_mem_no')
    be_eval_mem_no = models.IntegerField(null=False, blank=False, db_column='be_eval_mem_no')
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True)
    modf_dt = models.DateTimeField(blank=True, null=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eval_rel'

class AbltEvalQues(models.Model):
    eval_sheet_no = models.OneToOneField('EvalSheet', models.DO_NOTHING, db_column='eval_sheet_no', primary_key=True)
    ablt_ques_no = models.ForeignKey('AbltQuesPool', models.DO_NOTHING, db_column='ablt_ques_no')
    eval_trgt_clss = models.CharField(max_length=10)
    required_yn = models.CharField(max_length=1, blank=True, null=True)
    otpt_order = models.IntegerField(blank=True, null=True)
    ans_nmbr = models.IntegerField(blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, default='N', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ablt_eval_ques'
        unique_together = (('eval_sheet_no', 'ablt_ques_no', 'eval_trgt_clss'),)


class AbltQuesPool(models.Model):
    ablt_ques_no = models.AutoField(primary_key=True)
    eval_item_no = models.ForeignKey('EvalItem', models.DO_NOTHING, db_column='eval_item_no')
    question = models.CharField(max_length=200, blank=True, null=True)
    rslt_msr_type = models.CharField(max_length=10, blank=True, null=True)
    ans_type = models.CharField(max_length=10, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, default='N', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ablt_ques_pool'


class AbltEvalRslt(models.Model):
    eval_rel_no = models.OneToOneField('EvalRel', models.DO_NOTHING, db_column='eval_rel_no', primary_key=True)
    eval_sheet_no = models.ForeignKey('EvalSheet', models.DO_NOTHING, db_column='eval_sheet_no')
    ablt_ques_no = models.ForeignKey('AbltEvalQues', models.DO_NOTHING, db_column='ablt_ques_no')
    eval_trgt_clss = models.CharField(max_length=10, db_column='eval_trgt_clss')
    eval_plan_no = models.ForeignKey('EvalPlan', models.DO_NOTHING, db_column='eval_plan_no')
    ablt_eval_rslt = models.CharField(max_length=500, blank=True, null=True)
    eval_dt = models.DateTimeField(blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, default='N', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ablt_eval_rslt'
        unique_together = (('eval_rel_no', 'eval_sheet_no', 'ablt_ques_no', 'eval_trgt_clss'),)