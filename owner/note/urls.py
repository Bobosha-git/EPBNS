from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("page/<uuid:page_uuid>/", views.page, name="page"),
    path('create/', views.create_page, name='create_page'),
    path("delete/<uuid:page_uuid>/", views.delete_page, name="delete_page"),
]