from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from vacaplusapi.views import register_user, login_user
from vacaplusapi.views import VacaUsers, Locations, Activities, Users, LocationActivities

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'vacausers', VacaUsers, 'vacauser')
router.register(r'locations', Locations, 'location')
router.register(r'activities', Activities, 'activity')
router.register(r'users', Users, 'user')
router.register(r'locationactivities', LocationActivities, 'locationactivities')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user),
    path('login/', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]