from abc import ABC, abstractmethod


class AccountProfileRepository(ABC):

    # 프로필 생성에 필요한 정보들을 등록해주는 메서드 같네요~
    @abstractmethod
    def save(self, accout, nickname):
        pass