from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(user)
admin.site.register(Usercart)
admin.site.register(userProfile)
admin.site.register(productmain)
admin.site.register(productImage)
admin.site.register(userloginOTP)
admin.site.register(UserCartProduct)