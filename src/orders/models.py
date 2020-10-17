from django.db import models
import uuid

status_choices = [
    ('OPEN', 'OPEN'),  
    ('PENDING', 'PENDING'), #payment is sue from the customer end
    ('COMPLETE', 'COMPLETE')] 
class Order(models.Model):
    id                  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_code            = models.CharField(max_length=255, null=False)
    discount_elidgible  = models.BooleanField(default = False)
    discount_amount     = models.DecimalField(decimal_places=2, max_digits=1000)
    total_amount        = models.DecimalField(decimal_places=2, max_digits=1000)
    status              = models.CharField(max_length=25, 
                                default='OPEN', 
                                choices=status_choices)
    