from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50, default="")
    subcategoty=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=5000)
    pub_date=models.DateField()
    image=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=254)
    desc=models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=100,default=" ")
    email=models.CharField(max_length=111,default=" ")
    address=models.CharField(max_length=100,default=" ")
    city=models.CharField(max_length=100,default=" ")
    state=models.CharField(max_length=100,default=" ")
    zip_code=models.CharField(max_length=100,default=" ")
    phone=models.CharField(max_length=10,default=" ")

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=500,default="")
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:9]+"..."



