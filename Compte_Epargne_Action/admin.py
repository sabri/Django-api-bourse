from django.contrib import admin
from .models import Portfolio, PortfolioTitle


class PortfolioModeladmin(admin.ModelAdmin):
    list_display = ["title_name", "title_quantity", 'title_value', 'aquisition_date', 'time_stamp', "portolio_id"]
    search_fields = ["title_name"]

    class Meta:
        model = Portfolio


admin.site.register(Portfolio, PortfolioModeladmin)


class PortfolioTitleModeladmin(admin.ModelAdmin):
    list_display = ["portolio_id", "user_name",'portfolio_label']
    search_fields = ["portfolio_label"]

    class Meta:
        model = PortfolioTitle


admin.site.register(PortfolioTitle, PortfolioTitleModeladmin)
