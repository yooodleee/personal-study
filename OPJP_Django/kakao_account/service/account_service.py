from abc import ABC, abstractmethod


class AccountService(ABC):
    @abstractmethod
    def createAccount(self, email):
        pass