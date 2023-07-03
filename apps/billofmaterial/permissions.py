from rest_framework.permissions import BasePermission

class IsInfraArchitectApprover(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='INFRA_ARCHITECT_APPROVER_GROUP').exists()


class IsInfraArchitectVerifier(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='INFRA_ARCHITECT_VERIFIER_GROUP').exists()
