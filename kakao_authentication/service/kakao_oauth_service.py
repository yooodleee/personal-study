from abc import ABC, abstractmethod

class kakaoOauthService(ABC):

    @abstractmethod
    def requestkakaoOauthLink(self):
        pass
    
    @abstractmethod
    def requestAccessToken(self, code):
        pass