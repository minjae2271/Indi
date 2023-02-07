from django.db import models

class Type(models.Model):
    type = models.IntegerField()
    name = models.CharField(max_length=10)

class Company(models.Model):
    company_code = models.IntegerField()
    name = models.CharField(max_length=10)

class Ceiling(models.Model):
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    size = models.CharField(max_length=10)
    quantity = models.IntegerField(default= 0 , blank=True, null=False)

class Light(models.Model):
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    size = models.CharField(max_length=10)
    gender = models.BooleanField(default=False) #False: 암, True: 수
    quantity = models.IntegerField(default= 0 , blank=True, null=False)

class Acryl(models.Model):
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    size = models.CharField(max_length=10)
    fraction = models.BooleanField(default=False) #False: Center, True: Side
    quantity = models.IntegerField(default= 0 , blank=True, null=False)

class Mirror(models.Model):
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    size = models.CharField(max_length=10)
    quantity = models.IntegerField(default= 0 , blank=True, null=False)

class Pannel(models.Model):
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    size = models.CharField(max_length=10)
    quantity = models.IntegerField(default= 0 , blank=True, null=False)
    color = models.CharField(max_length=10)

class Subsidiary(models.Model):
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=10)
    quantity = models.IntegerField(default= 0 , blank=True, null=False)   


