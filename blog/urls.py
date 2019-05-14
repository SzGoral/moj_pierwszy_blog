from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list_ale_sprawdzam_gdzie_to_sie_wyswietla'),
    path('data', views.current_datetime, name='cotojest?'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]