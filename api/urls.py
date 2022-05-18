from django.urls import path, include
from rest_framework import routers
# from rest_framework.authtoken import views
from .views import UserDetailAPI,RegisterUserAPIView
from api.views import UserMessageViewSet

router = routers.DefaultRouter()

router.register(r'message',UserMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('api-token-auth/', views.obtain_auth_token),
    # path('message/', UserMessageViewSet.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('get-details/',UserDetailAPI.as_view()),
    path('register/',RegisterUserAPIView.as_view()),
]
