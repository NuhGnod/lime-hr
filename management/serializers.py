from rest_framework import serializers

from management.models import CommonCode, CommonMenu, CCode, CC2


class CommonCodeSerializer(serializers.ModelSerializer):
    class Meta :
        model = CommonCode
        fields = ['common_code','upper_code', 'lower_code']


class CommonMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonMenu
        fields = ['common_code','upper_menu', 'lower_menu']

class CCodeSerializer(serializers.ModelSerializer):
    class Meta :
        model = CCode
        fields = ['common_code','upper_code', 'lower_code']

class CC2Serializer(serializers.ModelSerializer):
    class Meta :
        model = CC2
        fields = ['common_code','parent_code', 'name', 'del_yn','created_at',
                  'modified_at', 'created_user', 'modified_user']


    def update(self, instance, validated_data):
        instance.created_user = validated_data.get('created_user', instance.created_user)




