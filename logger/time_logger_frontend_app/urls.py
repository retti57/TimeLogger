from django.urls import path
from . import views

APP_NAME = 'logger_frontend'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('tab/', views.TabView.as_view(), name='tab'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('logs/', views.logsview, name='logs'),
    path('createlog/', views.CreateLogView.as_view(), name='createlog'),

]