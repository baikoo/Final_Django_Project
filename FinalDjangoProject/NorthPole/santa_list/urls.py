from django.urls import path
from . import views

urlpatterns = [
    path('create-santas-list/', views.create_santas_list, name='create_santas_list'),
    path('view-santas-list/', views.view_santas_list, name='view_santas_list'),
    path('remove-child/<int:kid_id>/', views.remove_child, name='remove_child'),
    path('create-kid/', views.create_kid, name='create_kid'),
    path('view-all-kids/', views.view_all_kids, name='view_all_kids'),
    path('view-kid/<int:kid_id>/', views.view_kid, name='view_kid'),
]
