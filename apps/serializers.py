from rest_framework.serializers import ModelSerializer

from apps.models import Category


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "id", "title"
        
