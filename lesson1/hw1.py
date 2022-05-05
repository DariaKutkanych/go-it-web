from abc import ABC, abstractmethod
import pickle
import json


# Task No1

class SerializationInterface(ABC):

    def __init__(self, data):
        self.data = data

    @abstractmethod
    def save_data(self, file_name):
        print("Your iformation should be saved")


class SerializationJson(SerializationInterface):

    def save_data(self, file_name):

        with open(file_name, "w") as file:
            json.dump(self.data, file)


class SerializationBin(SerializationInterface):

    def save_data(self, file_name):
        with open(file_name, "wb") as file:
            pickle.dump(self.data, file)


# Task No2

class Meta(type):

    children_number = 0

    def __new__(*args):
        instance = type.__new__(*args)
        instance.class_number = Meta.children_number
        Meta.children_number += 1
        return instance


Meta.children_number = 0


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls3(metaclass=Meta):
    def __init__(self, data):
        self.data = data


assert (Cls1.class_number, Cls2.class_number, Cls3.class_number) == (0, 1, 2)
a, b, c = Cls1(''), Cls2(''), Cls3('')
assert (a.class_number, b.class_number, c.class_number) == (0, 1, 2)


if __name__ == "__main__":

    data = "let it be this text"

    file_json = SerializationJson(data)
    file_bin = SerializationBin(data)

    file_json.save_data("myfile.json")
    file_bin.save_data("myfile.bin")
