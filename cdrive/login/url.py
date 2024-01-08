from django.urls import path,include
from . import views
from rest_framework import routers
from .views import userViewset,bookmarkViewset

router=routers.DefaultRouter()
router.register(r'user',userViewset)

urlpatterns=[
    path('',views.index,name="index"),
    path('api',include(router.urls)),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('bookmark', views.bookmark, name="bookmark"),
    path('update',views.update,name="update"),
    path('addbookmark',views.addbookmark,name="addbookmark"),
    path('markerinput', views.markerinput, name="markerinput"),
    path('getmarker', views.getmarker, name="getmarker"),

]