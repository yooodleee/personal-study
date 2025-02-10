from abc import ABC, abstractmethod


class AccountRepository(ABC):

    # email을 인자로 받는 것을 보니 사용자 계정 정보에 email을 등록(save)해주는 작업을 해줄 것 같네요.
    @abstractmethod
    def save(self, email):
        pass

    # findById인 것으로 보아 이름 그대로 사용자 아이디(accountId)를 인자로 받아 어떤 작업을 할 것으로 보입니다.
    @abstractmethod
    def findById(self, accountId):
        pass