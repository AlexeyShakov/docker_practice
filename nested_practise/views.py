from .models import Avatar, Site, AccessKey, Profile, User
from .serializers import AvatarSerializer, SiteSerializer, AccessKeySerializer, ProfileSerializer, UserSerializer
from rest_framework import viewsets

# Create your views here.

class AvatarView(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer


class SiteView(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class AccessKeyView(viewsets.ModelViewSet):
     queryset = AccessKey.objects.all()
     serializer_class = AccessKeySerializer


class ProfileView(viewsets.ModelViewSet):
     queryset = Profile.objects.all()
     serializer_class = ProfileSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer   



