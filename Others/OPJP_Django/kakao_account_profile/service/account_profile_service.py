from abc import ABC, abstractmethod


class AccountProfileService(ABC):
    # 계정 프로필을 생성해주는 메서드일 것 같네요.
    @abstractmethod
    def createAccountProfile(self, accountId, nickname):
        pass