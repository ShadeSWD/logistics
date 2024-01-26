from rest_framework.pagination import PageNumberPagination


class VendorPagination(PageNumberPagination):
    page_size = 50
