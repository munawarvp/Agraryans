from unicodedata import category
from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class reg_table(models.Model):
    username=models.CharField(max_length=100)
    email_id=models.EmailField()
    password=models.CharField(max_length=10)
    con_password=models.CharField(max_length=10)
    contact_no=models.CharField(max_length=15)

    def __str__(self):
        return self.username

class add_reservation_form(models.Model):
    unique_no=models.CharField(max_length=20)
    item=models.CharField(max_length=30)
    datetime_From=models.CharField(max_length=30)
    datetime_To=models.CharField(max_length=30)
    status=models.CharField(max_length=30)

    def __str__(self):
        return self.item

class add_equipment_table(models.Model):
    eqp_name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    count=models.CharField(max_length=100)

    def __str__(self):
        return self.eqp_name
    
class add_package_table(models.Model):
    package_name=models.CharField(max_length=100)
    count=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    
    def __str__(self):
        return self.package_name

class add_category_table(models.Model):
    product_name=models.CharField(max_length=100)
    product_id=models.CharField(max_length=100)
    status=models.CharField(max_length=100)

    def __str__(self):
        return self.product_name

class add_user_table(models.Model):
    user_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    registration=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    status=models.CharField(max_length=100)

    def __str__(self):
        return self.user_name

class contact_form(models.Model):
    product_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    full_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    message=models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


