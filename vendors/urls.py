from rest_framework.routers import DefaultRouter
from vendors.apps import VendorsConfig
from vendors.views import VendorsViewSet


app_name = VendorsConfig.name

router = DefaultRouter()
router.register(r'vendors', VendorsViewSet, basename='vendors')

urlpatterns = [] + router.urls
