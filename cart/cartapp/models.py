from django.db import models

# Create your models here.

c= (
    ("male","male"),
    ("female","female"),
    ("others","others"),
    )
class user(models.Model):
    Phone_Number = models.CharField(max_length=10,unique=True)
    Email_ID = models.EmailField(null=False,blank=False)
    is_coustomer = models.BooleanField(null=False,blank=False)
    is_admin = models.BooleanField(null=False,blank=False)

class userProfile(models.Model):
    owner = models.OneToOneField(user,on_delete=models.CASCADE)
    Name = models.CharField(max_length=100,null=False,blank=False)
    Date_of_birth = models.DateField(auto_now=False,null=False,blank=False)
    Gender = models.CharField(choices=c,default='male',max_length=30)
    Image = models.ImageField(blank=False,null=False,upload_to='static/images')

class userloginOTP(models.Model):
    owner = models.ForeignKey(user,on_delete=models.CASCADE)
    otp = models.CharField(max_length=10,blank=False,null=False)
    active = models.BooleanField(default=1,blank=False)


class productmain(models.Model):
    Title = models.CharField(max_length=100,blank= False,null=False)
    Description = models.CharField(max_length=500,blank=False,null=False)
    unique_id = models.CharField(max_length=500,blank=False,null=False,unique=True)
    price = models.FloatField(blank=False,null=False)
    owner = models.ForeignKey(user,on_delete=models.CASCADE)


sc =(
    ('pending','pending'),
    ('completed','completed')
)
class UserCartProduct(models.Model):
    owner = models.OneToOneField(user,on_delete=models.CASCADE,default=1)
    product = models.ForeignKey(productmain,on_delete=models.CASCADE)
    status = models.CharField(choices=sc,default='pending',max_length=30)

class productImage(models.Model):
    product = models.ForeignKey(productmain,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images')

class Usercart(models.Model):
    owner = models.OneToOneField(user,on_delete=models.CASCADE)
    product = models.ManyToManyField(UserCartProduct,null=True)
    price =  price = models.FloatField(blank=True,null=True)