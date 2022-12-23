from django.shortcuts import render
from rest_framework import viewsets
from .models import banks,bank_branches,branches
from .serializer import banksserializer,branchserializer,bank_branchserializer

class banksviewsets(viewsets.ModelViewSet):
    queryset = banks.objects.all()
    serializer_class = banksserializer
    
class branchviewsets(viewsets.ModelViewSet):
    queryset = branches.objects.order_by()
    serializer_class = branchserializer



class bank_branchviewsets(viewsets.ModelViewSet):
    queryset = bank_branches.objects.all()
    serializer_class = bank_branchserializer
    