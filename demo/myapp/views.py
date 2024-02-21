from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.core.serializers import serialize as Serializer
import json
from datetime import datetime
# Create your views here.
class api(APIView):
    def get(self, request):
        invoices = Invoice.objects.all()
        invoiceDetails = InvoiceDetails.objects.all()
        invoices = Serializer('json', invoices)
        invoiceDetails = Serializer('json', invoiceDetails)
        return Response(invoiceDetails)

    def post(self, request):
        date = datetime.now()
        customer_name = request.data['customer_name']
        invoice = Invoice.objects.create(date=date, customer_name=customer_name)
        InvoiceDetails.objects.create(invoice = invoice, description = request.data['description'], quantity = request.data['quantity'], unitPrice = request.data['unitPrice'], price = request.data['price'])
        return Response("Invoice created successfully")
    def put(self, request):
        request = json.dumps(request)
        invoice = Invoice.objects.get(id=request.data['id'])
        invoice.customer_name = request.data['customer_name']
        invoice.save()
        invoice_detail = InvoiceDetails.objects.get(id=request.data['id'])
        invoice_detail.description = request.data['description']
        invoice_detail.quantity = request.data['quantity']
        invoice_detail.unitPrice = request.data['unitPrice']
        invoice_detail.price = request.data['price']
        invoice_detail.save()
        return Response("Invoice updated successfully")
    def delete(self, request):
        request = json.dumps(request)
        invoice = Invoice.objects.get(id=request.data['id'])
        invoice.delete()
        invoice_detail = InvoiceDetails.objects.get(invoice=request.data['id'])
        invoice_detail.delete()
        return Response("Invoice deleted successfully")