from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import ProjectViewSet, MeasurementViewSet

router = SimpleRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'measurements', MeasurementViewSet, basename='measurements')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
