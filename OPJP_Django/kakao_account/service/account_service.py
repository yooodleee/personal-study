from abc import ABC, abstractmethod


class AccountService(ABC):
    # 계정을 생성해주는 데 인자로 email을 받고 있습니다.
    @abstractmethod
    def createAccount(self, email):
        pass