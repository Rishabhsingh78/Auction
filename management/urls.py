from django.urls import path
from .views import *

urlpatterns = [
    path('auction_create/', create_auction, name='create_auction'),
    path('auctions_list/', auction_list, name='create_auaution_listction'),
    path('edit_auction/<int:auction_id>/', update_auction, name='update_auction'),
    path('closed_auction/<int:auction_id>/', close_auction, name='close_auction'),
]