from abc import ABC, abstractmethod


class Hash_Map(ABC):

    @abstractmethod
    def put(self, dado):
        pass

    @abstractmethod
    def get(self, dado):
        pass

    @abstractmethod
    def pop(self, dado):
        pass

    @abstractmethod
    def contains(self, dado):
        pass

    @abstractmethod
    def count(self, dado):
        pass