from django.db import models

# Create your models here
# decimal_places=5, max_digits=6,

class Pipe(models.Model):
    id = models.TextField('ID', primary_key=True)
    geometry = models.TextField('Pipeline Location', null=True)
    # wear = models.DecimalField('Wear',  decimal_places=6, max_digits=6, null=True)
    # weather = models.DecimalField('Weather',  decimal_places=6, max_digits=6, null=True)
    # vegetation = models.DecimalField('Vegetation',  decimal_places=6, max_digits=6, null=True)
    wear = models.TextField('Wear',   null=True) 
    weather = models.TextField('Weather',   null=True)
    vegetation = models.TextField('Vegetation',  null=True)
    names = models.TextField('Pipeline Name', null=True)
    risk = models.TextField('Risk',  null=True)
    
    # fat model, thin views

    
