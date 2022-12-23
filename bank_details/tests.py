from django.test import TestCase
from .models import branches,banks
from rest_framework.test import APITestCase
from rest_framework import status

class banks_post_Test(APITestCase):
    
    def test_post_banks(self):
        _data = {
            "name" : "123$"
        }
        # print(_data)s
        _response = self.client.post('/banks_info/banks/',data = _data,format = "json")
        
        _data = _response.json
        
        self.assertEqual(_response.status_code,status.HTTP_201_CREATED)

    def test_get_banks(self):
        _response = self.client.get('/banks_info/banks/')
        _data = _response.json()
        
        self.assertEqual(_response.status_code,status.HTTP_200_OK)
        

class branch_post_Test(APITestCase):
    
    def test_post_branch(self):
        self.ifsc = banks.objects.create(
            name = "123$",
        )
        
        _data = {
            "bank_id" : self.ifsc.name,
            "branch": "nikol",
            "address" : "sukan char rasta,opp. zingat , gujrat , ahmedabad",
            "city" : "Ahmedabad",
            "district": "Ahmedabad",
            "state" :  "Gujrat"     
        }
        # print(_data)s
        _response = self.client.post('/banks_info/branch/',data = _data,format = "json")
        
        _data = _response.json
        
        self.assertEqual(_response.status_code,status.HTTP_201_CREATED)

    def test_get_banks(self):
        _response = self.client.get('/banks_info/branch/')
        _data = _response.json()
        
        self.assertEqual(_response.status_code,status.HTTP_200_OK)



