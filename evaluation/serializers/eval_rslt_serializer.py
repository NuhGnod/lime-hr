from rest_framework import serializers
from mdm.models import AbltEvalRslt


class AbltEvalRsltSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbltEvalRslt
        fields = '__all__'
