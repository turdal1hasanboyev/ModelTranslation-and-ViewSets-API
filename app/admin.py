from django.contrib import admin
from .models import Book, User


admin.site.site_header = "Model Translations and ViewSets Admin Panel"
admin.site.site_title = "Model Translations and ViewSets Admin Panel"
admin.site.index_title = "Welcome to the Model Translations and ViewSets Dashboard!"

admin.site.register(Book)
admin.site.register(User)