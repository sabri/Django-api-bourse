from rest_framework import serializers
from .models import Title
from .models import CompanyDetail


class Titleserializers(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'


class CompanyDetailserializers(serializers.ModelSerializer):
    class Meta:
        model = CompanyDetail
        fields = '__all__'
