from django.urls import path
from . import views

APP_NAME = 'logger_frontend'

urlpatterns = [
    # registration
    path('home', views.home, name='home'),
    path('', views.home, name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('milperson/', views.MilpersonView.as_view(), name='milperson'),

    # log
    path('logs/', views.LogsListView.as_view(), name='logs'),
    path('createlog/', views.CreateLogView.as_view(), name='createlog'),
    path('log-update/<int:pk>/', views.LogUpdate.as_view(), name='log_update'),
    path('log/<int:pk>/', views.LogDetail.as_view(), name='log_detail'),
    path('createorder/', views.OrderCreate.as_view(), name='createorder'),

    # notes
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('notes/', views.NotesView.as_view(), name='notes'),
    path('addnotes/', views.AddNotesView.as_view(), name='addnotes'),

    # spiderpoints service
    path('spiderpoints/', views.spiderpoints, name='spiderpoints'),

]

