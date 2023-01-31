from rest_framework import serializers

from mdm.models import EvalPlan, EvalSheet
from management.models import CommCd


class GetEvalPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvalPlan
        fields = ['eval_plan_no', 'eval_plan_nm', 'eval_strt_dt', 'eval_end_dt']


class GetEvalPlanDetailSerializer(serializers.ModelSerializer):
    eval_clss_nm = serializers.SerializerMethodField(read_only=True)
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