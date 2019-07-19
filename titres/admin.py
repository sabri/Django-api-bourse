from django.contrib import admin

# Register your models h
from .models import Title
from .models import CompanyDetail


class TitleModeladmin(admin.ModelAdmin):
    list_display = ["title_name", "date_value", "current_value", "origin_value", "high_value", "low_value",
                    "opening_value",
                    "closing_value", "devise_value", "current_date", "quantity_title", "company_name"]
    search_fields = ["title_name"]

    class Meta:
        model = Title


class CompanyDetailModeladmin(admin.ModelAdmin):
    list_display = ["company_name","company_web", "company_phone", "company_web", "company_fullname"]
    search_fields = ["company_name"]

    class Meta:
        model = CompanyDetail


admin.site.register(Title, TitleModeladmin)
admin.site.register(CompanyDetail, CompanyDetailModeladmin)
