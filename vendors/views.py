from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from vendors.models import Dealer, Product
from vendors.serializers import DealerSerializer, ProductSerializer
from vendors.paginators import VendorPagination
from vendors.permissions import IsVendor


class VendorsViewSet(viewsets.ModelViewSet):
    serializer_class = DealerSerializer
    pagination_class = VendorPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['country']
    ordering_fields = ['country', 'city']
    permission_classes = [IsVendor, ]
    queryset = Dealer.objects.all()

    def perform_create(self, serializer):
        super().perform_create(serializer)
        new = serializer.save()
        new.owner = self.request.user
        new.save()


class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    pagination_class = VendorPagination
    permission_classes = [IsVendor, ]
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        super().perform_create(serializer)
        new = serializer.save()
        new.owner = self.request.user
        new.save()
