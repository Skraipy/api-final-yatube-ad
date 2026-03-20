from rest_framework.permissions import SAFE_METHODS, BasePermission


class ReadOnlyOrAuthorOnly(BasePermission):
    """
    Разрешает чтение всем, а изменение/удаление — только автору объекта.
    """

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj.author == request.user

