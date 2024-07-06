from django.db import models
from django.contrib.auth.models import User
from management.models import Auction
# Create your models here.
class Bids(models.Model):
    auction = models.ForeignKey(Auction,related_name='bids',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='bids',on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.bid_amount}'