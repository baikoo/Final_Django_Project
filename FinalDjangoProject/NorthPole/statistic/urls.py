from django.urls import path
from . import views

urlpatterns = [
    path('nice-and-naughty-count/', views.nice_and_naughty_counts, name='nice_and_naughty_count'),
    path('toys-and-kid-count/', views.toys_and_kid_counts, name='toys_and_kid_count'),
    path('time-to-make-toy/', views.time_to_make_toys, name='time_to_make_toy'),
    path('time-to-deliver-toy/', views.time_to_deliver_toys, name='time_to_deliver_toy'),
]
