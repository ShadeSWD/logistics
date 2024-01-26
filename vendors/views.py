from rest_framework import viewsets
from vendors.models import Dealer, Product
from vendors.serializers import DealerSerializer
from vendors.paginators import VendorPagination
from vendors.permissions import IsVendor


class VendorsViewSet(viewsets.ModelViewSet):
    serializer_class = DealerSerializer
    pagination_class = VendorPagination
    permission_classes = [IsVendor, ]
    queryset = Dealer.objects.all()

    def perform_create(self, serializer):
        super().perform_create(serializer)
        new = serializer.save()
        new.owner = self.request.user
        new.save()
