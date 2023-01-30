from rest_framework import serializers
from mdm.models import EvalPlan


class EvalPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvalPlan
        fields = ['eval_plan_no', 'eval_sheet_no', 'eval_plan_nm', 'eval_strt_dt', 'eval_end_dt']
