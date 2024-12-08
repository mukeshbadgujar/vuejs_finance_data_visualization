from rest_framework import generics, status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Invoice
from .serializers import InvoiceSerializer, InvoiceCreateSerializer
from rest_framework.response import Response
from django.db.models import Sum, F, FloatField, ExpressionWrapper
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

class InvoiceDashboardView(generics.ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'store_name', 'city', 'zip_code', 'store_location',
        'county_number', 'county', 'category', 'category_name',
        'vendor_number', 'vendor_name', 'item_number'
    ]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Calculate additional fields dynamically for each invoice
        response_data = []
        for invoice in queryset:
            stock = (invoice.pack or 0) * (invoice.bottle_volume_ml or 0)
            profit = ((invoice.state_bottle_retail or 0) - (invoice.state_bottle_cost or 0)) * (invoice.bottles_sold or 0)
            response_data.append({
                'invoice_number': invoice.invoice_number,
                'store_name': invoice.store_name,
                'city': invoice.city,
                'zip_code': invoice.zip_code,
                'category_name': invoice.category_name,
                'vendor_name': invoice.vendor_name,
                'item_number': invoice.item_number,
                'sales': invoice.sale_dollars,
                'stock': stock,
                'profit': profit,
            })

        return Response(response_data)


class AggregatedDashboardView(APIView):
    def get(self, request, *args, **kwargs):
        # Get the group_by parameter (city, county, or zip_code)
        group_by = request.query_params.get('group_by', 'city')

        if group_by not in ['city', 'county', 'zip_code']:
            return Response({'error': 'Invalid group_by value. Use "city", "county", or "zip_code".'}, status=400)

        # Calculate aggregated data
        queryset = (
            Invoice.objects.values(group_by)
            .annotate(
                total_stock=Sum(F('pack') * F('bottle_volume_ml'), output_field=FloatField()),
                total_sales=Sum('sale_dollars'),
                total_profit=Sum(
                    ExpressionWrapper(
                        (F('state_bottle_retail') - F('state_bottle_cost')) * F('bottles_sold'),
                        output_field=FloatField()
                    )
                )
            )
            .order_by(group_by)
        )

        # Format the response
        data = [
            {
                group_by: entry[group_by],
                'total_stock': entry['total_stock'] or 0,
                'total_sales': entry['total_sales'] or 0,
                'total_profit': entry['total_profit'] or 0
            }
            for entry in queryset
        ]

        return Response(data)


class AddInvoiceView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = InvoiceCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            # Save the invoice to the database
            serializer.save()
            return Response({"message": "Invoice added successfully!", "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ViewInvoiceView(APIView):
    def get(self, request, *args, **kwargs):
        invoice_id = request.query_params.get("id")
        invoice_number = request.query_params.get("invoice_number")
        
        # Fetch by ID
        if invoice_id:
            try:
                invoice = Invoice.objects.get(id=invoice_id)
                serializer = InvoiceCreateSerializer(invoice)
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
            except Invoice.DoesNotExist:
                return Response({"error": "Invoice with given ID not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Fetch by Invoice Number
        if invoice_number:
            try:
                invoice = Invoice.objects.get(invoice_number=invoice_number)
                serializer = InvoiceCreateSerializer(invoice)
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
            except Invoice.DoesNotExist:
                return Response({"error": "Invoice with given invoice number not found."},
                                status=status.HTTP_404_NOT_FOUND)
        
        # If no query parameter provided
        return Response({"error": "Provide either 'id' or 'invoice_number' as query parameter."},
                        status=status.HTTP_400_BAD_REQUEST)


class InvoicePagination(PageNumberPagination):
    page_size = 100  # Number of records per page
    page_size_query_param = 'page_size'  # Allow client to specify `page_size`
    max_page_size = 200  # Limit on the maximum number of records per page

class ViewAllInvoicesView(ListAPIView):
    queryset = Invoice.objects.all().order_by('-id')  # Fetch all invoices, ordered by latest
    serializer_class = InvoiceCreateSerializer
    pagination_class = InvoicePagination