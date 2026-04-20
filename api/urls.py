from django.urls import path 
from . import views


urlpatterns = [
    path("notes/",views.NotesListCreateAPIView.as_view()),
    path("notes/<int:product_id>/",views.NotesDetailAPIView.as_view()),
    path('users/', views.UserListAPIView.as_view()),
    
]