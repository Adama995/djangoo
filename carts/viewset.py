from rest_framework import viewsets
from carts.models import Cart
from carts.serializers.cart_serializer import CartSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class CartViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Cart.objects.all()
        serializer = CartSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
