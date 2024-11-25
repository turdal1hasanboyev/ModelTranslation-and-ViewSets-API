# translations py for model translation

# for model translations
from modeltranslation.translator import register, TranslationOptions
from .models import Book


@register(Book)
class BookTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'description', 'author')

# bu fayl yozilgandan song py manage.py makemigratios va py manage.py migrate berilishi shart