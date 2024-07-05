from rest_framework import serializers
from .models import *

class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ['id', 'title', 'description', 'starting_bid', 'current_bid', 'end_date', 'created_by', 'created_at','is_closed']
        read_only_fields = ['id', 'current_bid', 'created_by', 'created_at']

    def create(self,validated_data):
        validated_data['created_by'] = self.context['request'].user  # this is showing the creaetd user 
        validated_data['is_closed'] = validated_data.get('is_closed', False) # when the auction is created it will be unchecked
        return super().create(validated_data)
    

class Auction_list(serializers.ModelSerializer):
    class Meta:

        model = Auction
        fields = '__all__'

class UpdateAuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ['title', 'description', 'starting_bid', 'end_date']

    def update(self,instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance