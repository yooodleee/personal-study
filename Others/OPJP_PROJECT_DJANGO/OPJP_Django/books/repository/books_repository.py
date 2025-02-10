from abc import abstractmethod, ABC
import pandas as pd


class BooksRepository(ABC):

    @abstractmethod
    def create(self, bookData):
        pass

    @abstractmethod
    def save(self, bookData):
        pass