from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError


class CompanyDetail(models.Model):
    company_name = models.CharField(primary_key=True, unique=True, max_length=25)
    company_web = models.CharField(max_length=200)
    company_fullname = models.CharField(max_length=25, unique=True, null= False)
    company_photo = models.ImageField(upload_to='uploads', blank=True)
    company_phone = models.IntegerField(default=None)
    company_address = models.CharField(max_length=200)
    company_descp = models.TextField()
    company_industry = models.CharField(max_length=120)
    company_date_launch = models.DateField()

    def __unicode__(self):
        return self.company_name


def validate_even(value):
    if not CompanyDetail.objects.filter(company_name=value):
        raise ValidationError('enter valid name')


# Create your models here.
class Title(models.Model):
    title_name = models.CharField(max_length=50, validators=[validate_even])
    date_value = models.DateField()
    current_value = models.FloatField()
    origin_value = models.FloatField()
    high_value = models.FloatField()
    low_value = models.FloatField()
    opening_value = models.FloatField()
    closing_value = models.FloatField()
    devise_value = models.CharField(max_length=3)
    current_date = models.DateField(auto_now=False, auto_now_add=True)
    quantity_title = models.IntegerField()
    company_name = models.ForeignKey(CompanyDetail, on_delete=False, to_field='company_fullname', db_column='company_fullname', default=None)

    def __unicode__(self):
        return self.title_name

    def __str__(self):
        return self.title_name
