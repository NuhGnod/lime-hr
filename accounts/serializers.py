from rest_framework import serializers
from accounts.models import EusoMem
from management.models import CommCd, EusoDept

class GetEusoMemSerializer(serializers.ModelSerializer) :
    posi_nm = serializers.SerializerMethodField(read_only=True)
    duty_resp_nm = serializers.SerializerMethodField(read_only=True)
    dept_nm = serializers.SerializerMethodField(read_only=True)
    group_nm = serializers.SerializerMethodField(read_only=True)
    group_cd = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = EusoMem
        fields = ['id', 'username', 'name', 'posi_cd', 'posi_nm', 'duty_resp_cd', 'duty_resp_nm', 'dept_no', 'dept_nm',
                  'group_nm', 'group_cd']

    def get_posi_nm(self, obj):
        posi_cd = obj.posi_cd
        posi_nm = CommCd.objects.filter(comm_cd=posi_cd, del_yn='N').first()
        return str(posi_nm.cd_nm)

    def get_duty_resp_nm(self, obj):
        duty_resp_cd = obj.duty_resp_cd
        duty_resp_nm = CommCd.objects.filter(comm_cd=duty_resp_cd, del_yn='N').first()
        return str(duty_resp_nm.cd_nm)

    def get_dept_nm(self, obj):
        dept_no = obj.dept_no
        dept_qs = EusoDept.objects.filter(dept_no=dept_no, del_yn='N').first()
        return str(dept_qs.dept_nm)

    def get_group_nm(self, obj):
        dept_no = obj.dept_no
        dept_qs = EusoDept.objects.filter(dept_no=dept_no, del_yn='N').first()
        group_nm = CommCd.objects.filter(comm_cd=dept_qs.dept_cd, del_yn='N').first()
        return str(group_nm.cd_nm)

    def get_group_cd(self, obj):
        dept_no = obj.dept_no
        dept_qs = EusoDept.objects.filter(dept_no=dept_no, del_yn='N').first()
        return str(dept_qs.dept_cd)