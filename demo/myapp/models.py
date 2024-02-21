from django.db import models

# Create your models here.
class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    customer_name = models.CharField(max_length=100)

class InvoiceDetails(models.Model):
    id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unitPrice = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)