# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AbltEvalQues(models.Model):
    eval_sheet_no = models.IntegerField(primary_key=True)
    ablt_ques_no = models.ForeignKey('AbltQuesPool', models.DO_NOTHING, db_column='ablt_ques_no')
    eval_trgt_clss = models.CharField(max_length=10)
    eval_sheeteval_sheet_no = models.ForeignKey('EvalSheet', models.DO_NOTHING, db_column='eval_sheeteval_sheet_no')
    required_yn = models.CharField(max_length=1, blank=True, null=True)
    otpt_order = models.IntegerField(blank=True, null=True)
    ans_nmbr = models.IntegerField(blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ablt_eval_ques'
        unique_together = (('eval_sheet_no', 'ablt_ques_no', 'eval_trgt_clss', 'eval_sheeteval_sheet_no'),)


class AbltEvalRslt(models.Model):
    eval_rel_no = models.OneToOneField('EvalRel', models.DO_NOTHING, db_column='eval_rel_no', primary_key=True)
    ablt_ques_no = models.ForeignKey(AbltEvalQues, models.DO_NOTHING, db_column='ablt_ques_no')
    eval_sheet_no = models.ForeignKey(AbltEvalQues, models.DO_NOTHING, db_column='eval_sheet_no')
    eval_trgt_clss = models.ForeignKey(AbltEvalQues, models.DO_NOTHING, db_column='eval_trgt_clss')
    ablt_eval_queseval_sheeteval_sheet_no = models.ForeignKey(AbltEvalQues, models.DO_NOTHING, db_column='ablt_eval_queseval_sheeteval_sheet_no')
    eval_plan_no = models.ForeignKey('EvalPlan', models.DO_NOTHING, db_column='eval_plan_no')
    ablt_eval_rslt = models.CharField(max_length=500, blank=True, null=True)
    eval_dt = models.CharField(max_length=8, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ablt_eval_rslt'
        unique_together = (('eval_rel_no', 'ablt_ques_no', 'eval_sheet_no', 'eval_trgt_clss', 'ablt_eval_queseval_sheeteval_sheet_no'),)


class AbltQuesOpt(models.Model):
    ablt_ques_no = models.OneToOneField('AbltQuesPool', models.DO_NOTHING, db_column='ablt_ques_no', primary_key=True)
    ques_opt_cd = models.CharField(max_length=10)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ablt_ques_opt'
        unique_together = (('ablt_ques_no', 'ques_opt_cd'),)


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
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ablt_ques_pool'


class Ahp(models.Model):
    ahp_no = models.AutoField(primary_key=True)
    mem_no = models.ForeignKey('EusoMem', models.DO_NOTHING, db_column='mem_no')
    eval_item_no = models.ForeignKey('EvalItem', models.DO_NOTHING, db_column='eval_item_no')
    be_eval_item_no = models.ForeignKey('EvalItem', models.DO_NOTHING, db_column='be_eval_item_no')
    item_wght = models.IntegerField(blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ahp'


class Certification(models.Model):
    cert_no = models.AutoField(primary_key=True)
    cert_nm = models.CharField(max_length=100, blank=True, null=True)
    issu_orgn_nm = models.CharField(max_length=200, blank=True, null=True)
    sert_desc = models.CharField(max_length=200, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'certification'


class CommCd(models.Model):
    comm_cd = models.CharField(primary_key=True, max_length=10)
    hi_comm_cd = models.CharField(max_length=10)
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
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comm_cd'


class CompCarrEuso(models.Model):
    mem_no = models.OneToOneField('EusoMem', models.DO_NOTHING, db_column='mem_no', primary_key=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    dept_no = models.ForeignKey('EusoDept', models.DO_NOTHING, db_column='dept_no')
    occp_cd = models.CharField(max_length=10, blank=True, null=True)
    posi_cd = models.CharField(max_length=10, blank=True, null=True)
    mv_clss = models.CharField(max_length=10, blank=True, null=True)
    duty_resp_cd = models.CharField(max_length=10, blank=True, null=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comp_carr_euso'
        unique_together = (('mem_no', 'reg_dt'),)


class CompCarrOthr(models.Model):
    mem_no = models.OneToOneField('EusoMem', models.DO_NOTHING, db_column='mem_no', primary_key=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    occp_cd = models.CharField(max_length=10, blank=True, null=True)
    posi_cd = models.CharField(max_length=10, blank=True, null=True)
    comp_nm = models.CharField(max_length=100, blank=True, null=True)
    join_dt = models.CharField(max_length=8, blank=True, null=True)
    out_dt = models.CharField(max_length=8, blank=True, null=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comp_carr_othr'
        unique_together = (('mem_no', 'reg_dt'),)


class CsOrgn(models.Model):
    cs_no = models.AutoField(primary_key=True)
    zip_no = models.ForeignKey('ZipCd', models.DO_NOTHING, db_column='zip_no')
    cs_nm = models.CharField(max_length=100, blank=True, null=True)
    orgn_reg_no = models.CharField(max_length=13, blank=True, null=True)
    busir_no = models.CharField(max_length=10, blank=True, null=True)
    tel_no = models.IntegerField(blank=True, null=True)
    fax_no = models.IntegerField(blank=True, null=True)
    cs_addr = models.CharField(max_length=100, blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cs_orgn'


class DailyJobLog(models.Model):
    mem = models.OneToOneField('EusoMem', models.DO_NOTHING, primary_key=True)
    log_dt = models.CharField(max_length=8)
    job_cd = models.CharField(max_length=10, blank=True, null=True)
    job_desc = models.CharField(max_length=200, blank=True, null=True)
    reg_mem_no = models.ForeignKey('EusoMem', models.DO_NOTHING, db_column='reg_mem_no')
    modf_mem_no = models.ForeignKey('EusoMem', models.DO_NOTHING, db_column='modf_mem_no')
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_job_log'
        unique_together = (('mem', 'log_dt'),)


class DeptHist(models.Model):
    dept_hist_no = models.AutoField(primary_key=True)
    dept_no = models.ForeignKey('EusoDept', models.DO_NOTHING, db_column='dept_no')
    hi_dept_no = models.ForeignKey('EusoDept', models.DO_NOTHING, db_column='hi_dept_no')
    hist_desc = models.CharField(max_length=200, blank=True, null=True)
    dept_hist_clss = models.CharField(max_length=10, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dept_hist'


class EusoDept(models.Model):
    dept_no = models.AutoField(primary_key=True)
    dept_cd = models.CharField(max_length=10, blank=True, null=True)
    dept_nm = models.CharField(max_length=50, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'euso_dept'


class EusoMem(models.Model):
    mem_no = models.AutoField(primary_key=True)
    mem_nm = models.CharField(max_length=20)
    posi_cd = models.CharField(max_length=10, blank=True, null=True)
    duty_resp_cd = models.CharField(max_length=10, blank=True, null=True)
    dept_no = models.ForeignKey(EusoDept, models.DO_NOTHING, db_column='dept_no')
    zip_no = models.ForeignKey('ZipCd', models.DO_NOTHING, db_column='zip_no')
    mem_addr = models.CharField(max_length=100, blank=True, null=True)
    join_dt = models.CharField(max_length=8, blank=True, null=True)
    mem_stat_cd = models.CharField(max_length=10, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'euso_mem'


class EusoPjt(models.Model):
    pjt_no = models.AutoField(primary_key=True)
    cs_no = models.ForeignKey(CsOrgn, models.DO_NOTHING, db_column='cs_no')
    pjt_nm = models.CharField(max_length=100, blank=True, null=True)
    start_dt = models.CharField(max_length=8, blank=True, null=True)
    end_dt = models.CharField(max_length=8, blank=True, null=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'euso_pjt'


class EvalItem(models.Model):
    eval_item_no = models.AutoField(primary_key=True)
    eval_item_clss = models.CharField(max_length=10, blank=True, null=True)
    item_nm = models.CharField(max_length=100, blank=True, null=True)
    item_desc = models.CharField(max_length=200, blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eval_item'


class EvalPlan(models.Model):
    eval_plan_no = models.AutoField(primary_key=True)
    eval_sheet_no = models.IntegerField()
    eval_clss = models.CharField(max_length=10, blank=True, null=True)
    eval_plan_nm = models.CharField(max_length=100, blank=True, null=True)
    eval_plan_desc = models.CharField(max_length=200, blank=True, null=True)
    eval_strt_dt = models.CharField(max_length=8, blank=True, null=True)
    eval_end_dt = models.CharField(max_length=8, blank=True, null=True)
    s_eval_wght = models.IntegerField(blank=True, null=True)
    m_eval_wght = models.IntegerField(blank=True, null=True)
    j_eval_wght = models.IntegerField(blank=True, null=True)
    t_eval_wght = models.IntegerField(blank=True, null=True)
    p_eval_wght = models.IntegerField(blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)
    eval_sheeteval_sheet_no = models.ForeignKey('EvalSheet', models.DO_NOTHING, db_column='eval_sheeteval_sheet_no')

    class Meta:
        managed = False
        db_table = 'eval_plan'


class EvalRel(models.Model):
    eval_rel_no = models.AutoField(primary_key=True)
    eval_trgt_clss = models.CharField(max_length=10, blank=True, null=True)
    eval_mem_no = models.ForeignKey(EusoMem, models.DO_NOTHING, db_column='eval_mem_no')
    be_eval_mem_no = models.ForeignKey(EusoMem, models.DO_NOTHING, db_column='be_eval_mem_no')
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eval_rel'


class EvalSheet(models.Model):
    eval_sheet_no = models.AutoField(primary_key=True)
    eval_clss = models.CharField(max_length=10, blank=True, null=True)
    sheet_nm = models.CharField(max_length=100, blank=True, null=True)
    sheet_desc = models.CharField(max_length=200, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eval_sheet'


class KpiEvalQues(models.Model):
    kpi_ques_no = models.OneToOneField('KpiQuesPool', models.DO_NOTHING, db_column='kpi_ques_no', primary_key=True)
    eval_sheet_no = models.IntegerField()
    eval_trgt_clss = models.IntegerField()
    eval_sheeteval_sheet_no = models.ForeignKey(EvalSheet, models.DO_NOTHING, db_column='eval_sheeteval_sheet_no')
    required_yn = models.IntegerField(blank=True, null=True)
    otpt_order = models.IntegerField(blank=True, null=True)
    ans_nmbr = models.IntegerField(blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.IntegerField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.IntegerField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kpi_eval_ques'
        unique_together = (('kpi_ques_no', 'eval_sheet_no', 'eval_trgt_clss', 'eval_sheeteval_sheet_no'),)


class KpiQuesOpt(models.Model):
    kpi_ques_no = models.OneToOneField('KpiQuesPool', models.DO_NOTHING, db_column='kpi_ques_no', primary_key=True)
    ques_opt_cd = models.CharField(max_length=10)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kpi_ques_opt'
        unique_together = (('kpi_ques_no', 'ques_opt_cd'),)


class KpiQuesPool(models.Model):
    kpi_ques_no = models.AutoField(primary_key=True)
    eval_item_no = models.ForeignKey(EvalItem, models.DO_NOTHING, db_column='eval_item_no')
    question = models.CharField(max_length=200, blank=True, null=True)
    ans_type = models.CharField(max_length=10, blank=True, null=True)
    rslt_msr_type = models.CharField(max_length=10, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kpi_ques_pool'


class MemCert(models.Model):
    cert_no = models.OneToOneField(Certification, models.DO_NOTHING, db_column='cert_no', primary_key=True)
    acq_mem_no = models.ForeignKey(EusoMem, models.DO_NOTHING, db_column='acq_mem_no')
    acq_dt = models.CharField(max_length=8, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'mem_cert'
        unique_together = (('cert_no', 'acq_mem_no'),)


class MemSchl(models.Model):
    schl_no = models.OneToOneField('School', models.DO_NOTHING, db_column='schl_no', primary_key=True)
    mem_no = models.ForeignKey(EusoMem, models.DO_NOTHING, db_column='mem_no')
    enter_dt = models.CharField(max_length=8, blank=True, null=True)
    grad_dt = models.CharField(max_length=8, blank=True, null=True)
    schl_clss = models.CharField(max_length=8, blank=True, null=True)
    maj_cd = models.CharField(max_length=8, blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mem_schl'
        unique_together = (('schl_no', 'mem_no'),)


class MemTrain(models.Model):
    train_no = models.OneToOneField('Training', models.DO_NOTHING, db_column='train_no', primary_key=True)
    mem_no = models.ForeignKey(EusoMem, models.DO_NOTHING, db_column='mem_no')
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    strt_dt = models.CharField(max_length=8, blank=True, null=True)
    end_dt = models.CharField(max_length=8, blank=True, null=True)
    total_time = models.CharField(max_length=3, blank=True, null=True)
    train_rslt = models.CharField(max_length=100, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'mem_train'
        unique_together = (('train_no', 'mem_no', 'reg_dt'),)


class PKpiEvalRslt(models.Model):
    eval_rel_no = models.OneToOneField(EvalRel, models.DO_NOTHING, db_column='eval_rel_no', primary_key=True)
    kpi_ques_no = models.ForeignKey(KpiEvalQues, models.DO_NOTHING, db_column='kpi_ques_no')
    eval_sheet_no = models.ForeignKey(KpiEvalQues, models.DO_NOTHING, db_column='eval_sheet_no')
    eval_trgt_clss = models.ForeignKey(KpiEvalQues, models.DO_NOTHING, db_column='eval_trgt_clss')
    kpi_eval_queseval_sheeteval_sheet_no = models.ForeignKey(KpiEvalQues, models.DO_NOTHING, db_column='kpi_eval_queseval_sheeteval_sheet_no')
    eval_plan_no = models.ForeignKey(EvalPlan, models.DO_NOTHING, db_column='eval_plan_no')
    p_kpi_rslt = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    eval_dt = models.CharField(max_length=8, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_kpi_eval_rslt'
        unique_together = (('eval_rel_no', 'kpi_ques_no', 'eval_sheet_no', 'eval_trgt_clss', 'kpi_eval_queseval_sheeteval_sheet_no'),)


class PjtJoinHist(models.Model):
    join_hist_no = models.AutoField(primary_key=True)
    pjt_nm = models.CharField(max_length=100)
    mem_no = models.ForeignKey(EusoMem, models.DO_NOTHING, db_column='mem_no')
    role_cd = models.CharField(max_length=10, blank=True, null=True)
    enter_dt = models.CharField(max_length=8, blank=True, null=True)
    out_dt = models.CharField(max_length=8, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pjt_join_hist'


class School(models.Model):
    schl_no = models.AutoField(primary_key=True)
    schl_nm = models.CharField(max_length=100, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'school'


class SrvyPlan(models.Model):
    srvy_plan_no = models.AutoField(primary_key=True)
    srvy_sheet_no = models.ForeignKey('SrvySheet', models.DO_NOTHING, db_column='srvy_sheet_no')
    srvy_plan_nm = models.CharField(max_length=100, blank=True, null=True)
    srvy_plan_desc = models.CharField(max_length=200, blank=True, null=True)
    srvy_strt_dt = models.CharField(max_length=8, blank=True, null=True)
    srvy_end_dt = models.CharField(max_length=8, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'srvy_plan'


class SrvyQues(models.Model):
    srvy_sheet_no = models.OneToOneField('SrvySheet', models.DO_NOTHING, db_column='srvy_sheet_no', primary_key=True)
    srvy_ques_no = models.ForeignKey('SrvyQuesPool', models.DO_NOTHING, db_column='srvy_ques_no')
    required_yn = models.CharField(max_length=1, blank=True, null=True)
    otpt_order = models.IntegerField(blank=True, null=True)
    ans_nmbr = models.IntegerField(blank=True, null=True)
    ans_type = models.CharField(max_length=10, blank=True, null=True)
    rslt_msr_type = models.CharField(max_length=10, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'srvy_ques'
        unique_together = (('srvy_sheet_no', 'srvy_ques_no'),)


class SrvyQuesOpt(models.Model):
    srvy_ques_no = models.OneToOneField('SrvyQuesPool', models.DO_NOTHING, db_column='srvy_ques_no', primary_key=True)
    ques_opt_cd = models.CharField(max_length=10)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'srvy_ques_opt'
        unique_together = (('srvy_ques_no', 'ques_opt_cd'),)


class SrvyQuesPool(models.Model):
    srvy_ques_no = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'srvy_ques_pool'


class SrvyRslt(models.Model):
    mem_no = models.OneToOneField(EusoMem, models.DO_NOTHING, db_column='mem_no', primary_key=True)
    srvy_sheet_no = models.ForeignKey(SrvyQues, models.DO_NOTHING, db_column='srvy_sheet_no')
    srvy_ques_no = models.ForeignKey(SrvyQues, models.DO_NOTHING, db_column='srvy_ques_no')
    srvy_plan_no = models.ForeignKey(SrvyPlan, models.DO_NOTHING, db_column='srvy_plan_no')
    srvy_ans = models.CharField(max_length=500, blank=True, null=True)
    srvy_dt = models.CharField(max_length=8, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'srvy_rslt'
        unique_together = (('mem_no', 'srvy_sheet_no', 'srvy_ques_no'),)


class SrvySheet(models.Model):
    srvy_sheet_no = models.AutoField(primary_key=True)
    srvy_sheet_nm = models.CharField(max_length=100, blank=True, null=True)
    sheet_desc = models.CharField(max_length=200, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'srvy_sheet'


class TKpiEvalRslt(models.Model):
    dept_no = models.OneToOneField(EusoDept, models.DO_NOTHING, db_column='dept_no', primary_key=True)
    kpi_ques_no = models.ForeignKey(KpiEvalQues, models.DO_NOTHING, db_column='kpi_ques_no')
    eval_sheet_no = models.ForeignKey(KpiEvalQues, models.DO_NOTHING, db_column='eval_sheet_no')
    eval_trgt_clss = models.ForeignKey(KpiEvalQues, models.DO_NOTHING, db_column='eval_trgt_clss')
    kpi_eval_queseval_sheeteval_sheet_no = models.ForeignKey(KpiEvalQues, models.DO_NOTHING, db_column='kpi_eval_queseval_sheeteval_sheet_no')
    eval_plan_no = models.ForeignKey(EvalPlan, models.DO_NOTHING, db_column='eval_plan_no')
    t_kpi_rslt = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    eval_dt = models.CharField(max_length=8, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)
    del_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_kpi_eval_rslt'
        unique_together = (('dept_no', 'kpi_ques_no', 'eval_sheet_no', 'eval_trgt_clss', 'kpi_eval_queseval_sheeteval_sheet_no'),)


class Training(models.Model):
    train_no = models.AutoField(primary_key=True)
    train_nm = models.CharField(max_length=100, blank=True, null=True)
    train_desc = models.CharField(max_length=200, blank=True, null=True)
    train_orgn_nm = models.CharField(max_length=100, blank=True, null=True)
    edu_clss = models.CharField(max_length=10, blank=True, null=True)
    reg_mem_no = models.IntegerField(blank=True, null=True)
    modf_mem_no = models.IntegerField(blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'training'


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
    reg_dt = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modf_dt = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'zip_cd'
