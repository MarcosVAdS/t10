from django.db import models
from django.contrib.auth.models import User
from partner.models import Partner

class Debit(models.Model):
    CHOICES = (
        ('Canceled','Canceled'),
        ('Aproved','Aproved'),
        ('Rejected','Rejected'),
        ('Analyzing','Analyzing'),
    )
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.BigIntegerField(default=0)
    target = models.ForeignKey(Partner, on_delete=models.CASCADE)
    is_enable =  models.BooleanField()
    status = models.CharField(max_length=10, choices=CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['updated_at']