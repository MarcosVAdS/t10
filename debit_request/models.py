from django.db import models

# Create your models here.
class Debit(models.Model):
    #create_by = models.ForeignKey('auth.User', related_name='debit' )
    requester = models.CharField(max_length=244)
    value = models.BigIntegerField(default=0)
    target = models.CharField(max_length=14) ##should receive cnpj'
    is_enable =  models.BooleanField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['updated_at']