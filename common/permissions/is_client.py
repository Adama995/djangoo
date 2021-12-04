from rest_framework.permissions import BasePermission
from common.constants import CLIENTS


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name=CLIENTS).exists()
        )
