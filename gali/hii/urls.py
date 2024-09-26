from  django.urls import path
from . import views
urlpatterns=[
    path('a/',views.Student,name="Student"),
    path("m/", views.insert, name='insert'),
    path('update/<int:id>', views.update, name='update'),
    path('readall', views.readall, name='readall'),
    path('delete/<int:id>', views.del2, name='del2'),


]