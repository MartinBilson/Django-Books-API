from rest_framework import serializers
from .models import Book
import datetime
import re

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_date(self, value):
        """Ensure publication_date is in the past"""
        if value > datetime.date.today():
            raise serializers.ValidationError("Publication date cannot be in the future.")
        return value

    def validate_isbn(self, value):
        """Ensure ISBN is either 10 or 13 digits"""
        if not re.fullmatch(r'\d{10}|\d{13}', value):
            raise serializers.ValidationError("ISBN must be exactly 10 or 13 digits.")
        return value
