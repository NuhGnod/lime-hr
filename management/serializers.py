from rest_framework import serializers

from management.models import CommCd, EusoPjt
from accounts.models import EusoMem


class CommCdSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommCd
        fields=['comm_cd','hi_comm_cd','cd_nm','cd_desc','etc_1','etc_2','etc_3','alias_cd','reg_mem_no','modf_mem_no','del_yn']


class CommCdMapperSerializer(serializers.ModelSerializer) :
    class Meta:
        model = CommCd
        fields = ['comm_cd', 'cd_nm']


class EusoPjtSerializer(serializers.ModelSerializer):
    class Meta:
        model = EusoPjt
        fields = '__all__'