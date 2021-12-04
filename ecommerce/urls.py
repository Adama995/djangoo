from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, permissions
from articles.models import Article
from articles import viewset
from articles.serializers.article_serialiser import ArticleSerializer
from carts import viewset
from carts.models import Cart
from carts.serializers.cart_serializer import CartSerializer
from carts.viewset import CartSerializer

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="ECommerce API",
        default_version="v1",
        description="Description of my api",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
        
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CartViewset(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'carts', viewset.CartViewset, basename="carts")



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("admin/", admin.site.urls),
    path("carts/", include("carts.urls")),
    path("articles/", include("articles.urls")),
    path("api/", schema_view.with_ui("swagger", cache_timeout=0)),
]