from django.db import models

# Create your models here.
class  banks(models.Model):
    id = models.IntegerField(primary_key=True,null=False)
    name = models.CharField(max_length=49)
    
    def __str__(self):
            return self.name
    
    
class branches(models.Model):
    ifsc = models.CharField(primary_key=True,max_length=11)
    bank_id = models.ForeignKey(banks,on_delete=models.CASCADE)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)

    
class bank_branches(models.Model):
    bb_id = models.AutoField(primary_key=True)
    ifsc = models.ForeignKey(branches,on_delete=models.CASCADE)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)
    bank_name = models.CharField(max_length=49)