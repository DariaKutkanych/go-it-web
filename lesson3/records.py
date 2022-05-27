from field import Name, Phone, Email, Address, Birthday
from datetime import datetime


class Record:

    def __init__(self, name, address=None, phone=None, email=None, birthday=None):

        self.name = name if name.value else None
        self.addresses = []
        self.phones = []
        self.emails = []
        self.birthday = birthday

    def __repr__(self):
        if self.birthday:
            birthday = datetime.strftime(self.birthday.value, '%Y-%m-%d')
        else:
            birthday = None
        return f"{self.name}: {self.phones}, {self.emails}, {self.addresses}, {birthday}"

    def add_new_data(self, info, type_check, class_type):
        attributes = self.__dict__
        print(f'{info}, {type_check}, {class_type}')
        old_check = next(
            filter(lambda x: x.value == info, attributes[type_check]), None)

        if old_check:
            print(f"{info} has already been added")
        else:
            new_data = class_type(info)
            attributes[type_check].append(new_data)
            print(f"{new_data} for {self.name} has been added.")

    def add_address(self, address):
        self.add_new_data(address, "addresses", Address)

    def add_phone(self, phone):
        self.add_new_data(phone, "phones", Phone)

    def add_mail(self, mail):
        self.add_new_data(mail, "emails", Email)

    def change_data(self, old, new, type_check):

        attributes = self.__dict__
        new_num_check = next(
            filter(lambda x: x.value == new, attributes[type_check]), None)
        old_num = next(filter(lambda x: x.value ==
                       old, attributes[type_check]), None)

        if old_num and not new_num_check:
            old_num.value = new
            print(f"Number successfully changed to {old_num.value}")
        else:
            print("Old data not registered or new data already exist")

    def change_address(self, new_address, old_address):
        self.change_data(new_address, old_address, "addresses")

    def change_phone(self, new_num, old_num):
        self.change_data(new_num, old_num, "phones")

    def change_email(self, new_email, old_email):
        self.change_data(new_email, old_email, "emails")

    def change_birthday(self, new_birthday):
        self.birthday = new_birthday

    def delete_data(self, info, type_check):
        attributes = self.__dict__

        num = next(filter(lambda x: x.value ==
                   info, attributes[type_check]), None)
        if num:
            print(f"Параметр {num.value} видалений")
            if type_check == "phones":
                self.phones.remove(num)
            elif type_check == "emails":
                self.emails.remove(num)
            elif type_check == "addresses":
                self.addresses.remove(num)
        else:
            print("Такого параметру немає")

    def delete_number(self, phone):
        self.delete_data(phone, "phones")

    def delete_mail(self, mail):
        self.delete_data(mail, "emails")

    def delete_adress(self, address):
        self.delete_data(address, "addresses")

    def add_birthday(self, bd):
        self.birthday = Birthday(bd)
        print(f"{self.name} was born {bd}.")

    def __getstate__(self):
        attributes = self.__dict__.copy()
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
