from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)

from common.permissions import IsSeller, IsArticleOwner
from articles import models
from articles import serializers


class ArticleViewset(viewsets.ViewSet):
    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        elif self.action == "create":
            permission_classes = [IsSeller]
        elif self.action in ["update", "destroy"]:
            permission_classes = [IsArticleOwner]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    @swagger_auto_schema(
        responses={200: serializers.ArticleReponseSerializer(many=True)}
    )
    def list(self, request):
        queryset = models.Article.objects.all()
        serializer = serializers.ArticleReponseSerializer(queryset, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK)

    @swagger_auto_schema(
        request_body=serializers.AddArticleSerializer,
        responses={201: openapi.Response("The Article has been created")},
    )
    def create(self, request):
        serializer = serializers.AddArticleSerializer(data=request.data)
        if serializer.is_valid():
            models.Article.objects.create(
                name=serializer.validated_data["name"],
                price=serializer.validated_data["price"],
                owner=self.request.user,
            )

            return Response(status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={200: serializers.ArticleReponseSerializer()},
    )
    def retrieve(self, request, pk=None):
        queryset = models.Article.objects.get(pk=pk)
        serializer = serializers.ArticleReponseSerializer(queryset)

        return Response(serializer.data, status=HTTP_200_OK)

    def destroy(self, request, pk=None):
        article = models.Article.objects.get(pk=pk)
        self.check_object_permissions(request, article)
        article.delete()

        return Response(status=HTTP_204_NO_CONTENT)
