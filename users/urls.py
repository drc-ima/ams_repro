# from django.contrib.auth.views import PasswordChangeView
from django.urls import path, include
from . views import SignupView

app_name = 'user'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignupView.as_view(), name='signup'),
    # path('change-password/', PasswordChangeView.as_view(), name='password_change'),
]
