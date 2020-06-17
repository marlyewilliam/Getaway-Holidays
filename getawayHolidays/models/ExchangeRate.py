from django.db import models


class ExchangeRate(models.Model):
    base_currency = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=20, decimal_places=6)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return '%s to %s' % (self.base_currency, self.currency)

    class Meta:
        app_label = 'getawayHolidays'