from rest_framework.routers import DefaultRouter
from vendors.apps import VendorsConfig
from vendors.views import VendorsViewSet, ProductsViewSet


app_name = VendorsConfig.name

router = DefaultRouter()
router.register(r'vendors', VendorsViewSet, basename='vendors')
router.register(r'products', ProductsViewSet, basename='products')

urlpatterns = [] + router.urls
