from django.urls import path
from . import views
from .views import StudyspacesListView, StudyspacesCreateView, StudyspacesDetailView 

urlpatterns = [
    #URLs para registro y sesion
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('studyspace/list/', views.StudyspacesListView.as_view(), name='studyspaces_list'),
    path('studyspace/create/', views.StudyspacesCreateView.as_view(), name='studyspace_create'),
    path('studyspace/<int:pk>/', views.StudyspacesDetailView.as_view(), name='studyspace_detail'),

   
]   
