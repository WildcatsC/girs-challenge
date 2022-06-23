from email.policy import default
from django.db import models

# Create your models here.
class Pipe(models.Model):
    geometry = models.JSONField(null=False, default = dict)
    wear = models.DecimalField(decimal_places=5, max_digits=6, null=False, default=0)
    weather = models.DecimalField(decimal_places=5, max_digits=6, null=False, default=0)
    vegetation = models.DecimalField(decimal_places=5, max_digits=6, null=False, default=0)
    names = models.CharField(max_length=50, default = '', unique=True)

    # fat model, thin views
    
