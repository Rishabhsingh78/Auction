from rest_framework import serializers
from .models import Bids
class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bids

        fields = ['id', 'auction', 'user', 'bid_amount', 'bid_time']
        read_only_fields = ['id', 'user', 'bid_time']
        extra_kwargs = {
            'auction': {'required': False}
        }


    def validate_bid_amount(self,value):
        auction = self.context['auction']
        if value <= auction.current_bid:
            raise serializers.ValidationError("Bid amount must be higher than the current bid.")
        return value
    
   
    def create(self, validated_data):
        auction = self.context['auction']
        validated_data['auction'] = auction
        validated_data['user'] = self.context['request'].user
        auction.current_bid = validated_data['bid_amount']
        auction.save()
        return super().create(validated_data)
    

class BidListSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Bids
        fields = '__all__'