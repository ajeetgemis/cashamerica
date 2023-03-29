from rest_framework import serializers
from .models import registercustomer


class serialdata(serializers.ModelSerializer):
    class Meta:
        model=registercustomer
        fields="__all__"