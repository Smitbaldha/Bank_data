from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import banksviewsets,branchviewsets,bank_branchviewsets

router= routers.DefaultRouter()
router.register(r'banks',banksviewsets)
router.register(r'branch',branchviewsets)
router.register(r'bank_branch',bank_branchviewsets)




urlpatterns = [
    path('',include(router.urls))
]
