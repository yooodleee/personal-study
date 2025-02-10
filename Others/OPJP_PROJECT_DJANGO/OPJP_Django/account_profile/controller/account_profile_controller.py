from django.shortcuts import render
from rest_framework import viewsets, status

from ..service.account_profile_service_impl import AccountProfileServiceImpl


# Create your views here.
class AccountProfileController(viewsets.ViewSet):
    __accountProfileService = AccountProfileServiceImpl.getInstance()