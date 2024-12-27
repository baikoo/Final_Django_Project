from django.urls import path
from . import views

urlpatterns = [
    path('create-toy/<int:kid_id>/', views.create_toy, name='create_toy'),
    path('view-all-toys/', views.view_all_toys, name='view_all_toys'),
    path('view-toy/<int:toy_id>/', views.view_toy, name='view_toy'),
    path('generate-gift/<int:kid_id>/', views.generate_gift, name='generate_gift'),
]
