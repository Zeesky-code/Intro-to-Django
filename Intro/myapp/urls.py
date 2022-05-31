from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path('', views.home, name= "index"),
    path('add/<int:a>/<int:b>',views.add, name="add"),
    path('intro/<str:name>/<int:age>', views.intro, name="intro"),
    path('second', views.second, name="second"),
    path('third', views.third, name="third"),
    path('imagepage',views.imagepage, name="imagepage"),
    path('imagepage2', views.imagepage2, name="imagepage2"),
    path('imagepage3', views.imagepage3, name="imagepage3"),
    path('imagepage4', views.imagepage4, name="imagepage4"),
    path('imagepage5/<str:imagename>', views.imagepage5, name="imagepage5"),
    path('myform',views.myform, name="myform"),
    path('submitmyform',views.submitmyform, name="submitmyform"),
]