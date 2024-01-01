from django.db import models

# Create your models here.

class company(models.Model):
    id=models.CharField(primary_key=True,max_length=50)
    uwi=models.TextField()
    data_type=models.IntegerField()
    x=models.TextField()
    y=models.TextField()
    data_source_year=models.TextField()
    created_on=models.TextField()
    updated_on=models.TextField()