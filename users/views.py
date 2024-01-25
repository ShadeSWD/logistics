from rest_framework import viewsets
from users.models import User
from users.serializers import UserSerializer
from users.paginators import UserPagination
from users.permissions import IsStaff


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    pagination_class = UserPagination
    permission_classes = [IsStaff, ]
    queryset = User.objects.all()

    def perform_create(self, serializer):
        super().perform_create(serializer)
        new = serializer.save()
        new.set_password(new.password)
        new.save()
