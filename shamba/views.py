from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User,LandOwner,LandInformation
import jwt, datetime
from .serializers import LandInformationSerializer,LandOwnerSerializer
from rest_framework import status
from django.http import Http404


# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes = {
        'register':'register/',
        'login':'login/',
        'user':'user/',
        'logout':'logout/',
        'land-information':'land-information/',
        'land-information':'land-information/<int:pk>/',
        'land-detail':'land-detail/',
        'land-detail':'land-detail/<int:pk>/',
        
    }
    return Response(routes)

class RegisterView(APIView):
  def post(self,request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

class LoginView(APIView):
  def post(self,request):
    email = request.data['email']
    password = request.data['password']

    user = User.objects.get(email=email)
    if user is None:
      raise AuthenticationFailed('User not found')
    if user.check_password(password):
      raise AuthenticationFailed('Incorrect password!')    

    payload = {
      'id':user.id,
      'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
      'iat':datetime.datetime.utcnow()
    }

    token = jwt.encode(payload,'secret',algorithm='HS256')
# .decode('utf-8')
    response = Response()

    response.set_cookie(key='jwt',value=token,httponly=True)
    response.data = {
      'jwt':token
    } 

    return response
    
class UserView(APIView):
  def get(self,request):
    token = request.COOKIES.get('jwt')

    if not token:
      raise AuthenticationFailed('Unauthenticated')
    
    try:
      payload = jwt.decode(token,'secret',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
      raise AuthenticationFailed('Unauthenticated')

    user = User.objects.filter(id=payload['id']).first()
    serializer = UserSerializer(user)

    return Response(serializer.data)

class LogoutView(APIView):
  def post(self,request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
      'message':'success'
    }
    return response

class LandInfoView(APIView):
  def get(self,request,format=None):
    landInfo = LandInformation.objects.all()
    serializer = LandInformationSerializer(landInfo,many=True)
    return Response(serializer.data)

  def post(self,request,format=None):
    serializer = LandInformationSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LandInfoDetailView(APIView):
  def get_object(self,pk):
    try:
      return LandInformation.objects.get(id=pk)
    except LandInformation.DoesNotExist:
      raise Http404

  def get(self,request,pk,format=None):
    landDetails = self.get_object(pk)
    serializer = LandInformationSerializer(landDetails)
    return Response(serializer.data)

  def put(self,request,pk,format=None):
    landDetails = self.get_object(pk)
    serializer = LandInformationSerializer(landDetails,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self,request,pk,format=None):
    landDetails = self.get_object(pk)
    landDetails.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class LandOwnerInformationView(APIView):
  def get(self,request,format=None):
    landOwners = LandOwner.objects.all()
    serializer = LandOwnerSerializer(landOwners, many=True)
    return Response(serializer.data)

  def post(self,request,format=None):
    serializer = LandOwnerSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LandOwnerDetailInfoView(APIView):
  def get_object(self,pk):
    try:
      return LandOwner.objects.get(id=pk)
    except LandOwner.DoesNotExist:
      raise Http404
    
  def get(self, request, pk, format=None):
    landOwner = self.get_object(pk)
    serializer = LandOwnerSerializer(landOwner)
    return Response(serializer.data)

  def put(self,request,pk,format=None):
    landOwner = self.get_object(pk)
    serializer = LandOwnerSerializer(landOwner,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self,request,pk,format=None):
    landOwner = self.get_object(pk)
    landOwner.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

