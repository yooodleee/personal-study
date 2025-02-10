from rest_framework import serializers

# 일단 이 부분은 pass 할게요~
class KakaoOauthAccessTokenSerializer(serializers.Serializer):
    code = serializers.CharField()