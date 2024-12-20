from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Проверка автора(увидел в пачке)."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


# Для проверки регистрации пользователя.
# Ещё проврека автора комма или поста.
PERMISSIONS = (IsAuthenticated, IsOwnerOrReadOnly,)
