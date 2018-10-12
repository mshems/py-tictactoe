from abc import ABCMeta, abstractmethod


class AbstractState(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __hash__(self):
        pass

    @abstractmethod
    def result(self, action):
        pass

    @abstractmethod
    def actions(self):
        pass

    @abstractmethod
    def max(self):
        pass

    @abstractmethod
    def terminal(self):
        pass

    @abstractmethod
    def evaluate(self):
        pass


class AbstractAction(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def legal(self, state):
        pass
