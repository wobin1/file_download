from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('books/', views.book_list),
    path('music/', views.music),
    path('video/', views.video),
    path('book_upload/', views.book_upload),
]