from rest_framework import serializers

class kakaoOauthAccessTokenSerializer(serializers.Serializer):
    code=serializers.CharField()