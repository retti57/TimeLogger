from django.urls import path
from . import views

APP_NAME = 'logger_frontend'

urlpatterns = [
    path('home', views.home, name='home'),
    path('',views.home, name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('milperson/', views.MilpersonView.as_view(), name='milperson'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('logs/', views.logsview, name='logs'),
    path('log/<int:pk>/', views.LogDetail.as_view(), name='log_detail'),
    path('createlog/', views.CreateLogView.as_view(), name='createlog'),
    path('spiderpoints/', views.spiderpoints, name='spiderpoints'),
    path('notes/', views.NotesView.as_view(), name='notes'),
    path('addnotes/', views.AddNotesView.as_view(), name='addnotes'),
]
