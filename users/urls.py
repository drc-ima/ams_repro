# from django.contrib.auth.views import PasswordChangeView
from django.urls import path, include
# from django.views.generic import TemplateView

from ams.views import dashboard
from users import views
from .views import SignupView, CreateProfile

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignupView.as_view(), name='signup'),
    path('change-password/', views.change_password, name='change_passwords'),
    path('dashboard/', dashboard.Count.as_view(template_name='users/dashboard.html'), name='dashboard'),
    path('profile-create/', CreateProfile.as_view(), name='profile'),
    path('password-change/', views.change_password, name='change_password'),
]
