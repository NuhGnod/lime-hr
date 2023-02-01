from datetime import datetime
from rest_framework import serializers

from mdm.models import EvalPlan, EvalSheet
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

from rest_framework import serializers

from management.models import CommCd
from management.serializers import CommCdSerializer
from mdm.models import EvalSheet, AbltEvalQues, AbltQuesPool, EvalItem


class EvalSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvalSheet
        fields = ['eval_sheet_no',
                  'eval_clss',
                  'sheet_nm',
                  'sheet_desc',
                  'reg_mem_no',
                  'modf_mem_no',
                  'reg_dt',
                  'modf_dt',
                  'del_yn']


class getQues(serializers.ModelSerializer):
    class Meta:
        model = EvalSheet
        fields = ['eval_sheet_no',
                  'eval_clss',
                  'sheet_nm',
                  'sheet_desc',
                  'reg_mem_no',
                  'modf_mem_no',
                  'del_yn']


class AbltQuesPoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbltQuesPool
        fields = '__all__'


class EvalItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvalItem
        fields = '__all__'


class joinEvalItemSerializer(serializers.ModelSerializer):
    cd_nm = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = EvalItem
        fields = ['eval_item_no',
                  'eval_item_clss',
                  'item_nm',
                  'item_desc',
                  'reg_mem_no',
                  'modf_mem_no',
                  'del_yn',
                  'cd_nm']

    def get_cd_nm(self, obj):
        eval_item_clss = obj.eval_item_clss
        comm_cd = CommCd.objects.filter(comm_cd=eval_item_clss).first()
        return str(comm_cd.cd_nm)


class joinSerializer(serializers.ModelSerializer):
    eval_item_no = joinEvalItemSerializer(allow_null=True)
    ans_type_nm = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = AbltQuesPool
        fields = ['ablt_ques_no',
                  'eval_item_no',
                  'question',
                  'rslt_msr_type',
                  'reg_mem_no',
                  'modf_mem_no',
                  'del_yn',
                  'ans_type',
                  'ans_type_nm']

    def get_ans_type_nm(self, obj):
        ans_type = obj.ans_type
        type = CommCd.objects.filter(comm_cd=ans_type).first()
        return str(type.cd_nm)


class createAbltEvalQuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbltEvalQues
        fields = '__all__'


class getAbltEvalQuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbltEvalQues
        fields = ['eval_sheet_no',
                  'ablt_ques_no',
                  'eval_trgt_clss',
                  'required_yn',
                  'otpt_order',
                  'del_yn',
                  'ans_nmbr',
                  'modf_mem_no',
                  'reg_mem_no',
                  ]
class AbltEvalQuesSerializer(serializers.ModelSerializer):
    ablt_ques_no = joinSerializer(allow_null=True)
    eval_trgt_clss_nm = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = AbltEvalQues
        fields = ['eval_sheet_no',
                  'ablt_ques_no',
                  'eval_trgt_clss',
                  'required_yn',
                  'otpt_order',
                  'del_yn',
                  'ans_nmbr',
                  'modf_mem_no',
                  'reg_mem_no',
                  'eval_trgt_clss_nm'
                  ]

    def get_eval_trgt_clss_nm(self, obj):
        trgt = obj.eval_trgt_clss
        first = CommCd.objects.filter(comm_cd=trgt).first()
        return str(first.cd_nm)
