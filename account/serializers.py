from abc import ABC

from rest_framework import serializers
from account.models import User, UserProfile
from django_countries.serializer_fields import CountryField


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('professional', 'dob', 'address', 'country', 'city', 'zip', 'photo', 'cin', 'phone')
        country = CountryField(country_dict=True)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

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
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.professional = profile_data.get('professional', profile.professional)
        profile.dob = profile_data.get('dob', profile.dob)
        profile.cin = profile_data.get('cin', profile.cin)
        profile.address = profile_data.get('address', profile.address)
        profile.country = profile_data.get('country', profile.country)
        profile.city = profile_data.get('city', profile.city)
        profile.zip = profile_data.get('zip', profile.zip)
        profile.photo = profile_data.get('photo', profile.photo)
        profile.phone = profile_data.get('phone', profile.phone)

        profile.save()

        return instance


