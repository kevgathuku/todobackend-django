from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(
        required=True, allow_blank=False, max_length=256)
    completed = serializers.BooleanField(required=False, default=False)
    url = serializers.URLField()

    def create(self, validated_data):
        """
        Create and return a new `Todo` instance, given the validated data.
        """
        return Todo.objects.create(**validated_data)
