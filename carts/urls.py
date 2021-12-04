from rest_framework import routers
from . import viewset

router = routers.DefaultRouter()

router.register("", viewset.CartViewset, basename="carts")
urlpatterns = router.urls
