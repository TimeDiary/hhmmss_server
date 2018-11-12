from django.conf import settings
from snippets.models import Location
from django.contrib.auth.models import AbstractUser as User
from snippets.serializers import LocationSerializer, UserSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_202_ACCEPTED
from oauth2client import client, crypt


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LocationList(ListCreateAPIView):
    queryset = Location.ojbects.all()
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def perfrom_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Location.objects.filter(owner=user)


class Login(APIView):
    def verifyGoogleToken(self, idToken):
        isIdTokenValid = True
        try:
            idinfo = client.verify_id_token(idToken, settings.CLIENT_ID)
            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise crypt.AppIdentityError("Wrong issuer.")
        except crypt.AppIdentityError:
            # Invalid token
            isIdTokenValid = False
            idinfo = {
                'Response': 'Invalid Google Token!',

            }
        return (isIdTokenValid, idinfo)

    def post(self, request, format=None):
        isIdTokenValid, googleResponse = self.verifyGoogleToken(request.data.get('id_token'))
        if isIdTokenValid:
            try:
                user = User.objects.get(email=googleResponse.get('email'))
                token = Token.objects.get(user=user)
                statusCode = HTTP_202_ACCEPTED
            except User.DoesNotExist:
                user = User.objects.create(username=googleResponse.get('name'), email=googleResponse.get('email'))
                token = Token.objects.create(user=user)
                statusCode = HTTP_201_CREATED
            additionalContent = {
                'token': token.key,

            }
            googleResponse.update(additionalContent)
            return Response(googleResponse, statusCode)
        else:
            return Response(googleResponse, status=HTTP_400_BAD_REQUEST)
