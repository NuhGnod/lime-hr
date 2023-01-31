from rest_framework import serializers

from management.models import CommCd, EusoPjt, PjtJoinHist, CsOrgn
from accounts.models import EusoMem


class CommCdSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommCd
        fields=['comm_cd','hi_comm_cd','cd_nm','cd_desc','etc_1','etc_2','etc_3','alias_cd','reg_mem_no','modf_mem_no','del_yn']


class CommCdMapperSerializer(serializers.ModelSerializer) :
    class Meta:
        model = CommCd
        fields = ['comm_cd', 'cd_nm']


class GetCsOrgnSerializer(serializers.ModelSerializer):
    class Meta:
        model = CsOrgn
        fields = ['cs_no', 'cs_nm']


class EusoPjtSerializer(serializers.ModelSerializer):
    class Meta:
        model = EusoPjt
        fields = '__all__'


class CreatePjtSerializer(serializers.ModelSerializer):
    class Meta:
        model = EusoPjt
        fields = ['pjt_nm', 'cs_no', 'start_dt', 'end_dt', 'reg_mem_no', 'modf_mem_no']

    def validate(self, attrs):
        if len(attrs['pjt_nm']) == 0:
            raise serializers.ValidationError("프로젝트 명을 입력해주세요")
        else:
            return attrs


class GetPjtJoinMemberSerializer(serializers.ModelSerializer):
    mem_nm = serializers.SerializerMethodField(read_only=True)
    role_nm = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = PjtJoinHist
        fields = ['join_hist_no', 'pjt_no', 'mem_no', 'mem_nm', 'role_nm', 'enter_dt', 'out_dt']

    def get_mem_nm(self, obj):
        mem_no = obj.mem_no
        mem_qs = EusoMem.objects.filter(username=mem_no, del_yn='N').first()
        return str(mem_qs.name)

    def get_role_nm(self, obj):
        role_cd = obj.role_cd
        role_qs = CommCd.objects.filter(comm_cd=role_cd, del_yn='N').first()
        return str(role_qs.cd_nm)


class CreatePjtJoinMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PjtJoinHist
        fields = ['pjt_no', 'mem_no', 'role_cd', 'enter_dt', 'out_dt', 'reg_mem_no', 'modf_mem_no']

    def validate(self, attrs):
        pjt_join_hist_qs = PjtJoinHist.objects.filter(pjt_no=attrs['pjt_no'], mem_no=attrs['mem_no'], del_yn='N')
        if pjt_join_hist_qs.exists():
            raise serializers.ValidationError("이미 프로젝트에 참여된 인력")
        return attrs


class DelPjtJoinMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PjtJoinHist
        fields = ['join_hist_no', 'mem_no', 'del_yn', 'modf_mem_no']