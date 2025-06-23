from rest_framework import serializers
from .models import Todoitems


class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todoitems
        fields = ['id', 'title', 'description', 'completed']
      