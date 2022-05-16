from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from api.views import UserMessageViewSet

router = routers.DefaultRouter()

router.register(r'api',UserMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('message/',ViewNameWillbehere),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
    # path('api-auth/', include('rest_framework.urls')),
