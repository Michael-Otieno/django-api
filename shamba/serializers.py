from rest_framework import serializers
from .models import User,LandInformation,LandOwner


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id','first_name','last_name','id_number','phone_number','email']

  extra_kwargs = {
    'password': {'write_only':True}
  }

  def create(self,validated_password):
    password = validated_password.pop('password',None)
    instance = self.Meta.model(**validated_password)
    if password is not None:
      instance.set_password(password)
    instance.save()
    return instance

  

class LandInformationSerializer(serializers.ModelSerializer):
  class Meta:
    model = LandInformation
    fields = '__all__'

class LandOwnerSerializer(serializers.ModelSerializer):
  class Meta:
    model = LandOwner
    fields = '__all__'