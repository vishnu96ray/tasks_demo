from django.urls import path, include
from api import  views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('School', views.SchoolViewSet)
router.register('Route', views.RouteViewSet)



urlpatterns = [
    path('api/', include(router.urls)),

]

