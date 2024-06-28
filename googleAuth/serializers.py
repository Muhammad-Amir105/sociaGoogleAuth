from rest_framework import serializers


class IdTokenSerializer(serializers.Serializer):
    id_token = serializers.CharField()
