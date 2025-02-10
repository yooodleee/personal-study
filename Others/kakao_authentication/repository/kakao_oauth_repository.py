from abc import ABC, abstractmethod

class kakaoOauthRepository(ABC):

    @abstractmethod
    def getOauthLink(self):
        pass

    @abstractmethod
    def getAccessToken(self, code):
        pass