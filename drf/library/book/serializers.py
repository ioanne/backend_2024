from rest_framework import serializers

from book.models import Book

class BookSerializer(serializers.ModelSerializer):
    full_title = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "publication_date",
            "isbn",
            "pages",
            "full_title",
        ]

    def get_full_title(self, obj):
        return f"{obj.title} by {obj.author}"
