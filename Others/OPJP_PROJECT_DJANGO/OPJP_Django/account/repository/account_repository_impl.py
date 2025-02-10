from django.core.exceptions import ObjectDoesNotExist

from account.entity.account import Account
from account.entity.account_role_type import AccountRoleType
from account.entity.role_type import RoleType
from account.repository.account_repository import AccountRepository


class AccountRepositoryImpl(AccountRepository):
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
    
    def save(self, email):
        defaultRoleType, created = AccountRoleType.objects.get_or_create(
            roleType=RoleType.NORMAL
        )

        account = Account(email=email, roleType=defaultRoleType)
        account.save()
        return account
    
    def findById(self, accountId):
        try:
            return Account.objects.get(id=accountId)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist(
                f'Account ID {accountId} 존재하지 않음.'
            )
    
    def findByEmail(self, email):
        try:
            return Account.objects.get(email=email)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist(
                f"Account {email} 존재하지 않음."
            )