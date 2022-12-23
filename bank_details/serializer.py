from rest_framework import serializers
from .models import banks,branches,bank_branches

class banksserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=banks
        fields="__all__" 

class branchserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=branches
        fields="__all__" 
        
class bank_branchserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=bank_branches
        fields="__all__"