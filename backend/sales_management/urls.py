from django.urls import path
from .views import InvoiceDashboardView, AggregatedDashboardView, AddInvoiceView, ViewInvoiceView, ViewAllInvoicesView

urlpatterns = [
    path('invoice/', InvoiceDashboardView.as_view(), name='invoice-dashboard'),
    path('aggregated-dashboard/', AggregatedDashboardView.as_view(), name='aggregated-dashboard'),
    path('add-invoice/', AddInvoiceView.as_view(), name='add-invoice'),
    path('view-invoice/', ViewInvoiceView.as_view(), name='view-invoice'),
    path('view-all-invoices/', ViewAllInvoicesView.as_view(), name='view-all-invoices'),

]
