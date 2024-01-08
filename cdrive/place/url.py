from django.urls import path,include
from . import views
from rest_framework import routers
from .views import tourViewset,restaurantViewset

router=routers.DefaultRouter()
router.register(r'api',tourViewset)
router.register(r'api',restaurantViewset)



urlpatterns=[
    path('tourfind',views.tourfind,name="tourfind"),
    path('restaurantfind',views.restaurantfind,name="restaurantfind"),
    path('tourinput',views.tourinput,name="tourinput"),
    path('restaurantinput',views.restaurantinput,name="restaurantinput"),
    path('tour',include(router.urls)),
    path('restaurant', include(router.urls)),

]