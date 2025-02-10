from abc import ABC, abstractmethod


class ReceiverService(ABC):
    @abstractmethod
    def requestToInjectClientSocket(self):
        pass

    @abstractmethod
    def requestToReceiveClient(self):
        pass
