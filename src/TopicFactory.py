from abc import ABC, abstractmethod


class TopicFactory(ABC):

    @abstractmethod
    def giveInfo(self):
        pass

    @abstractmethod
    def Bonus(self):
        pass