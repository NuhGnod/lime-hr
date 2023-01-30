from rest_framework import serializers
from accounts.models import EusoMem
from management.models import CommCd

class GetEusoMemSerializer(serializers.ModelSerializer) :
    posi_nm = serializers.SerializerMethodField(read_only=True)
    duty_resp_nm = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = EusoMem
        fields = ['id', 'username', 'name', 'posi_cd', 'posi_nm', 'duty_resp_cd', 'duty_resp_nm']

    def get_posi_nm(self, obj):
        posi_cd = obj.posi_cd
        posi_nm = CommCd.objects.filter(comm_cd=posi_cd, del_yn='N').first()
        return str(posi_nm.cd_nm)

    def get_duty_resp_nm(self, obj):
        duty_resp_cd = obj.duty_resp_cd
        duty_resp_nm = CommCd.objects.filter(comm_cd=duty_resp_cd, del_yn='N').first()
        return str(duty_resp_nm.cd_nm)