import django_filters
from rest_framework import serializers
from rest_framework.utils import json
from rest_framework.viewsets import ReadOnlyModelViewSet

from training1.models import Log


class JSONSerializerField(serializers.Field):
    """ Serializer for JSONField -- required to make field writable"""

    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return json.loads(value)


class LogSerializer(serializers.HyperlinkedModelSerializer):
    input_detail = JSONSerializerField()
    output_detail = JSONSerializerField()

    class Meta:
        model = Log
        fields = ('action_code', 'application_code', 'alt_module_name', 'input_detail', 'output_detail')


class LogViewSet(ReadOnlyModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    filter_fields = ('action_code', 'application_code')
