from rest_framework import serializers
from articles import models


class ArticleReponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = serializers.ALL_FIELDS
