from django.urls import path
from . import views

APP_NAME = 'logger_frontend'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('tab/', views.TabView.as_view(), name='tab'),
    path('tab2/', views.tab2, name='tab2'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('milperson/', views.MilpersonView.as_view(), name='milperson'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('logs/', views.logsview, name='logs'),
    path('log/<int:pk>/', views.LogDetail.as_view(), name='log_detail'),
    # path('log/<int:pk>/', views.detaillog, name='log_detail'),
    path('createlog/', views.CreateLogView.as_view(), name='createlog'),
    path('spiderpoints/', views.spiderpoints, name='spiderpoints'),
]
