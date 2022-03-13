from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/signup/', views.signUpView, name='signup'),
    path('account/login/', views.loginView, name='login'),
    path('account/logout/', views.logoutView, name='logout'),
    path('create/', views.create, name='create'),
    path('notes_list/', views.notes_list, name='notes_list'),
    path('remove/<int:note_id>/', views.remove_note, name='remove'),
]