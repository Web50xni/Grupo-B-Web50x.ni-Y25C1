from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('studyspace/<str:title>/', views.studyspace_view, name='studyspace'),
    path('studyspace/create/', views.create_studyspace_view, name='create'),
]
