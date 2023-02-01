from datetime import datetime
from rest_framework import serializers

from mdm.models import EvalPlan, EvalSheet, EvalItem, AbltQuesPool
from management.models import CommCd


class GetEvalPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvalPlan
        fields = ['eval_plan_no', 'eval_plan_nm', 'eval_strt_dt', 'eval_end_dt']


class GetEvalPlanDetailSerializer(serializers.ModelSerializer):
    eval_clss_nm = serializers.SerializerMethodField(read_only=True)
    eval_strt_dt = serializers.SerializerMethodField(read_only=True)
    eval_end_dt = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = EvalPlan
        fields = [
            'eval_plan_no', 'eval_plan_nm', 'eval_plan_desc', 'eval_strt_dt', 'eval_end_dt', 'eval_sheet_no',
            'eval_clss', 'eval_clss_nm', 'sf_eval_wght', 's_eval_wght', 'm_eval_wght', 'j_eval_wght', 't_eval_wght', 'p_eval_wght'
        ]

    def get_eval_clss_nm(self, obj):
        eval_clss = obj.eval_clss
        eval_clss_qs = CommCd.objects.filter(comm_cd=eval_clss, del_yn='N').first()
        return str(eval_clss_qs.cd_nm)

    def get_eval_strt_dt(self, obj):
        eval_strt_dt = obj.eval_strt_dt.strftime("%m/%d/%Y")
        return eval_strt_dt

    def get_eval_end_dt(self, obj):
        eval_end_dt = obj.eval_end_dt.strftime("%m/%d/%Y")
        return eval_end_dt


class GetEvalSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvalSheet
        fields = ['eval_sheet_no', 'eval_clss', 'sheet_nm']


class CreateEvalPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvalPlan
        fields = ['eval_plan_nm', 'eval_plan_desc', 'eval_strt_dt', 'eval_end_dt', 'eval_sheet_no', 'eval_clss',
                  'sf_eval_wght', 's_eval_wght', 'm_eval_wght', 'j_eval_wght', 't_eval_wght', 'p_eval_wght',
                  'reg_mem_no', 'modf_mem_no'
            ]


class EvalItemSerializer(serializers.ModelSerializer):
    cd_nm = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = EvalItem
        fields = [
            'eval_item_no',
            'eval_item_clss',
            'item_nm',
            'item_desc',
            'reg_dt',
            'modf_dt',
            'reg_mem_no',
            'modf_mem_no',
            'del_yn',
            'cd_nm'
        ]

    def get_cd_nm(self, obj):
        eval_item_clss = obj.eval_item_clss
        comm_cd = CommCd.objects.filter(comm_cd=eval_item_clss).first()
        return str(comm_cd.cd_nm)


class QuesPoolSerializer(serializers.ModelSerializer):
    eval_item_no = EvalItemSerializer(read_only=True)

    class Meta:
        model = AbltQuesPool
        fields = '__all__'


class CreateQuesPoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = AbltQuesPool
        fields = [
            'eval_item_no',
            'question',
            'rslt_msr_type',
            'ans_type',
            'reg_mem_no',
            'modf_mem_no',
        ]
