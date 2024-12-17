from django.db import IntegrityError

from account_profile.entity.account_profile import AccountProfile
from account_profile.repository.account_profile_repository import AccountProfileRepository


class AccountProfileRepositoryImpl(AccountProfileRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def save(self, account, nickname):
        try:
            accountProfile = AccountProfile.objects.create(account=account, nickname=nickname)
            return accountProfile

        except IntegrityError:
            raise IntegrityError(f"Nickname '{nickname}' 이미 존재함.")