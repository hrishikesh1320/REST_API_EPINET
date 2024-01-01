from rest_framework import serializers
from api.models import company
class companyserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = company
        fields="__all__"