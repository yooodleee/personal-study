from rest_framework import serializers
from subscription.entity.subscription import Subscription


# 실제 사용할 데이터의 형식이 무엇인지 알려줍니다.
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            'subscriptionId',
            'subscriptionName',
            'subscriptionDescription'
            'subscriptionPrice',
            'subscriptionImage',
            'registeredDate',
            'updatedDate'
        ]
        read_only_fields = ['registeredDate', 'updatedDate']