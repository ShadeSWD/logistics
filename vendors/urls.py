from rest_framework.routers import DefaultRouter
from vendors.apps import VendorsConfig


app_name = VendorsConfig.name

router = DefaultRouter()
# router.register(r'users', UsersViewSet, basename='users')

urlpatterns = [] + router.urls
