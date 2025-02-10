from abc import ABC, abstractmethod


class ReceiverRepository(ABC):
    @abstractmethod
    def injectClientSocket(self, clientSocket):
        pass

    @abstractmethod
    def receive(self, clientSocketObject):
        pass
