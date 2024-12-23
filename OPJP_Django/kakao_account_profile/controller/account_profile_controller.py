from django.http import JsonResponse
from rest_framework import viewsets, status

from ..service.account_profile_service_impl import AccountProfileServiceImpl


class AccountProfileController(viewsets.ViewSet):
    __accountProfileService = AccountProfileServiceImpl.getInstance()