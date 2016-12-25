from django.conf.urls import url, include
from rest_framework import routers
from . import views


# # Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'humidity',views.HumidityViewSet)
router.register(r'temperatures',views.TemperatureViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]