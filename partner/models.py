from django.db import models

class Partner(models.Model):
    name = models.CharField(max_length=244)
    cnpj = models.CharField(max_length=14)
    use_automatic_debit = models.BooleanField(default=False)
    is_enable = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['updated_at']