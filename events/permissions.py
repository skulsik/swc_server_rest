from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """ Проверка на владельца, если владелец открывает доступ """
    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True

        return False
