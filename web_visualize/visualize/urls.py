from django.urls import path
from . import views

app_name = 'visualize'
urlpatterns = [
    path('', views.index, name="index"),
    path('view/<label_group>', views.view_images, name="view"),
    path('search',views.search, name="search")
]