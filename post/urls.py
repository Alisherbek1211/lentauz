from django.urls import path,include
from rest_framework import routers
from post.views import PostViewSet,CategoryViewSet,CompanyViewSet

router = routers.SimpleRouter()
router.register(r'post',PostViewSet)
router.register(r'category',CategoryViewSet)
router.register(r'company',CompanyViewSet)


urlpatterns = [
    path('api/v1/',include(router.urls)),
]
