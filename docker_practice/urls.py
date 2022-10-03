"""docker_practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from publications.views import PublicationsView, TemplateView, CategoryView
from nested_practise.views import AvatarView, SiteView, AccessKeyView, ProfileView, UserView
from unique_practice.views import ChildView, ParentView

router = DefaultRouter()
router.register(r'public', PublicationsView)
router.register(r'template', TemplateView)
router.register(r'category', CategoryView)


router.register(r'avatar', AvatarView)
router.register(r'site', SiteView)
router.register(r'access', AccessKeyView)
router.register(r'profile', ProfileView)
router.register(r'user', UserView)


router.register(r"child", ChildView)
router.register(r"parent", ParentView)



urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls