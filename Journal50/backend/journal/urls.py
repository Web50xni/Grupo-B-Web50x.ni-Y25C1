from django.urls import path
from . import views

urlpatterns = [
    #URLs para registro y sesion
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    #URLs de studyspace
    path('studyspace/list/', views.studyspace_list_view, name='studyspace_list'),
    path('studyspace/create/', views.studyspace_create_view, name='studyspace_create'),
    path('studyspace/<str:title>/', views.studyspace_detail_view, name='studyspace_detail'),
    path('studyspace/<str:title>/update/', views.studyspace_update_view, name='studyspace_update'),
    path('studyspace/<str:title>/delete/', views.studyspace_delete_view, name='studyspace_delete'),

    #URLs de note
    path('note/<str:studyspace>/<str:title>/', views.note_detail_view, name='note_detail'),
]   
