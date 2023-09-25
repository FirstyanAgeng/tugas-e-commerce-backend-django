from rest_framework import generics, authentication, permissions 
from user.serializers import UserSerializer 
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from user.serializers import AuthTokenSerializer, UserSerializer 
from rest_framework.settings import api_settings 
from rest_framework import viewsets, status
from rest_framework.views import APIView
from core.models import User 


class CreteUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer 
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES 

class ManageUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer 
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserRoleView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    
    def get(self, request):
        id = request.user.id
        role = request.user.role  
        name = request.user.name
        phone_number = request.user.phone_number
        response_data = {
            'id': id,
            'role': role,
            'name': name,
            'phone_number': phone_number
        }

        return Response(response_data, status=status.HTTP_200_OK)