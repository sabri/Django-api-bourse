from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from titres.models import CompanyDetail


class PortfolioTitle(models.Model):
    portolio_id = models.AutoField(primary_key=True, unique=True, default=None, )
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='portfolio',
                                  to_field='email', db_column='email')
    portfolio = (
        ('p1', 'A'),
        ('p2', 'B'),
        ('p3', 'C'),
        ('p4', 'D'),
        ('p5', 'E'),
    )
    portfolio_label = models.CharField(choices=portfolio, default=None, max_length=2)

    def __unicode__(self):
        return self.portolio_id


class Portfolio(models.Model):
    portolio_id = models.ForeignKey(PortfolioTitle, on_delete=models.CASCADE, related_name='portfolioTitle',)
    title_name = models.ForeignKey(CompanyDetail, on_delete=models.CASCADE, db_column='company_name', to_field='company_name')
    title_quantity = models.IntegerField()
    title_value = models.FloatField()
    aquisition_date = models.DateField()
    time_stamp = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title_name
