from rest_framework import serializers
from .models import User, Portfolio, PortfolioTitle


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class PortfolioTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioTitle
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = PortfolioTitleSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        PortfolioTitle.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.title_name = profile_data.get('title_name', profile.title_name)
        profile.title_quantite = profile_data.get('title_quantity', profile.title_quantite)
        profile.title_value = profile_data.get('title_value', profile.title_value)
        profile.aquisition_date = profile_data.get('aquisition_date', profile.aquisition_date)
        profile.time_stamp = profile_data.get('time_stamp', profile.time_stamp)
        profile.save()

        return instance
