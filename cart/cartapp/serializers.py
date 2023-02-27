from .models import *
from rest_framework import serializers

class userserializer(serializers.ModelSerializer):

    class Meta:
        model = user
        fields = '__all__'

class usercartserializer(serializers.ModelSerializer):

    class Meta:
        model = Usercart
        fields = '__all__'

class productserializer(serializers.ModelSerializer):

    class Meta:
        model = productmain
        fields = '__all__'

class productimgserializer(serializers.ModelSerializer):

    class Meta:
        model = productImage
        fields = '__all__'

class userloginotpserializer(serializers.ModelSerializer):
    class Meta:
        model = userloginOTP
        fields = '__all__'