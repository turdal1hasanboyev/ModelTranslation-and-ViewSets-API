from rest_framework.viewsets import ModelViewSet # viewset api yozish uchun
from .models import Book, User
from .serializers import BookModelViewSetSerializer, UserModelViewSetSerializer


class BookViewSetAPIView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelViewSetSerializer
    lookup_field = 'pk'


class UserViewSetAPIView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelViewSetSerializer
    lookup_field = 'pk'