from django.db import models
from datetime import date

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20)
    date = models.DateField(default=date.today)
    store_number = models.IntegerField(null=True, blank=True)
    store_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    store_location = models.CharField(max_length=255, null=True, blank=True)
    county_number = models.IntegerField(null=True, blank=True)
    county = models.CharField(max_length=100)
    category = models.IntegerField(null=True, blank=True)
    category_name = models.CharField(max_length=255)
    vendor_number = models.IntegerField(null=True, blank=True)
    vendor_name = models.CharField(max_length=255)
    item_number = models.IntegerField(null=True, blank=True)
    item_desc = models.CharField(max_length=255)
    pack = models.IntegerField(null=True, blank=True)
    bottle_volume_ml = models.IntegerField(null=True, blank=True)
    state_bottle_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    state_bottle_retail = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    bottles_sold = models.IntegerField(null=True, blank=True)
    sale_dollars = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    volume_sold_liters = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    volume_sold_gallons = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    
    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.store_name}"
