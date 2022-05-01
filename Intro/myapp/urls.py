from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name= "index"),
    path('add/<int:a>/<int:b>',views.add, name="add"),
    path('intro/<str:name>/<int:age>', views.intro, name="intro"),
    path('second', views.second, name="second"),
    path('third', views.third, name="third")
]