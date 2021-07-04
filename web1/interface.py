from abc import ABC, abstractmethod
import pickle
import json
from typing import Dict, List, Tuple


class SerializationInterface(ABC):

    @abstractmethod
    def to_json(self, *args, **kwargs):
        pass

    @abstractmethod
    def to_bin(self, *args, **kwargs):
        pass


class ListSerialization(SerializationInterface, List):

    def to_json(self, *args, **kwargs):
        obj = json.dumps(self)
        return obj

    def to_bin(self, *args, **kwargs):
        obj = pickle.dumps(self)
        return obj


class DictSerialization(SerializationInterface, Dict):

    def to_json(self, *args, **kwargs):
        obj = json.dumps(self)
        return obj

    def to_bin(self, *args, **kwargs):
        obj = pickle.dumps(self)
        return obj


class TupleSerialization(SerializationInterface, Tuple):
    def to_json(self, *args, **kwargs):
        return super().to_json(*args, **kwargs)


def example():
    my_list = ListSerialization()

    my_list.append('dkfjf')

    print(my_list.to_json())

    my_dict = DictSerialization()

    my_dict['first'] = 'First Data'

    print(my_dict.to_bin())


if __name__ == '__main__':
    example()