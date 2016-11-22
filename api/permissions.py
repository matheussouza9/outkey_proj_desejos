from rest_framework import permissions

class IsSuperuserOrBasicForUser(permissions.BasePermission):
    # message = 'lorem ipsum'

    def has_permission(self, request, view):
        # se nao for super usuario, nao deixa fazer post nem delete
        if request.method in ('POST', 'DELETE') and not request.user.is_superuser:
            return False

        return True

    def has_object_permission(self, request, view, user):
        # se nao for super usuario, so deixa fazer get ou put nos seus proprios dados
        if request.method in ('GET', 'PUT') and not request.user.is_superuser:
            return user == request.user

        return True