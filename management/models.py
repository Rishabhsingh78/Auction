from django.db import models
from django.contrib.auth.models import User

class Auction(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    end_date = models.DateTimeField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default = True)

    def save(self, *args, **kwargs):
        if self.current_bid == 0:
            self.current_bid = self.starting_bid
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title