from rest_framework import routers

from . import viewset

router = routers.DefaultRouter()
router.register("", viewset.ArticleViewset, basename="articles")

urlpatterns = router.urls
