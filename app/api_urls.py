from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSetAPIView, UserViewSetAPIView


router = DefaultRouter()
router.register(r'books', BookViewSetAPIView)
router.register(r'users', UserViewSetAPIView)
# bu yo'l vazifasini bajaradi

urlpatterns = [
    path('', include(router.urls)),
    # routerni yo'li
]