from django.urls import path
from .views import HomeView, CreateUserView, SignUpView, ContactFormView, TabView

APP_NAME = 'logger_frontend'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('createuser/', CreateUserView.as_view(), name='createuser'),
    path('tab/', TabView.as_view(), name='tab'),
    path('contact/', ContactFormView.as_view(), name='contact'),

]