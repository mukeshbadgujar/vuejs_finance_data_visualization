from django.contrib import admin
from .models import Invoice

class InvoiceAdmin(admin.ModelAdmin):
    # Fields to show in the list view (list display)
    list_display = ('id', 'invoice_number', 'store_name', 'date', 'sale_dollars', 'bottles_sold')

    # Fields to show in the form view (adding or editing)
    # fields = ('invoice_number', 'date', 'store_name', 'address', 'city', 'sale_dollars')

    # Alternatively, you can use fieldsets to group fields
    # fieldsets = (
    #     (None, {
    #         'fields': ('invoice_number', 'date')
    #     }),
    #     ('Store Info', {
    #         'fields': ('store_name', 'address', 'city', 'zip_code', 'store_location')
    #     }),
    #     ('Financial Info', {
    #         'fields': ('sale_dollars', 'bottles_sold')
    #     }),
    # )

    # You can also use exclude to exclude certain fields from being shown
    # exclude = ('field_to_exclude',)

# Register the custom admin class with the model
admin.site.register(Invoice, InvoiceAdmin)
