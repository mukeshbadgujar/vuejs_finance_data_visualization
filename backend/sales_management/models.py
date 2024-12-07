from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    location = models.CharField(max_length=255)

class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=255)
    item_number = models.CharField(max_length=100)

class Stock(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Sales(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    profit = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
