"""ams_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from braces.views import LoginRequiredMixin
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

import ams.urls as ams_urls
import users.urls as users_urls


class LayoutView(LoginRequiredMixin, TemplateView):
    template_name = 'layout.html'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ams/', include(ams_urls, namespace='ams')),
    path('', LayoutView.as_view(), name='home'),
    path('users/', include(users_urls, namespace='users')),
]
