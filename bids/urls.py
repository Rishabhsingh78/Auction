from django.urls import path
from .views import place_bid,bids_list

urlpatterns = [
    path('place_bid/<int:auction_id>/', place_bid, name='place_bid'),
    path('bids_list/', bids_list, name='bid_list'),
]
