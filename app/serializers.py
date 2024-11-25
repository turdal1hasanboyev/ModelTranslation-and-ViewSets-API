from rest_framework.serializers import ModelSerializer # default serializer
from .models import Book, User


class BookModelViewSetSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # barchasini olish


class UserModelViewSetSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'