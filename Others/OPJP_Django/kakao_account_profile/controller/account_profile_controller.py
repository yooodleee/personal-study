from django.http import JsonResponse
from rest_framework import viewsets, status

from ..service.account_profile_service_impl import AccountProfileServiceImpl


# 일단 이부분은 pass할게여여
class AccountProfileController(viewsets.ViewSet):
    __accountProfileService = AccountProfileServiceImpl.getInstance()