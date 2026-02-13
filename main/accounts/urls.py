from django.urls import path
from django.contrib.auth import views as auth_views

from .views import signup, logout_view
from .forms import CustomAuthenticationForm

app_name = 'accounts'

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html', 
            authentication_form=CustomAuthenticationForm,
        ),
        name='login',
    ),
    path(
        'logout/',
        logout_view,
        name='logout',
    ),
    path(
        'signup/',
        signup,
        name='signup',
    ),
]

