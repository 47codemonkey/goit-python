from collections import UserDict


class Name:
    name = ''


class Phone:
    phone = ''


class Record:
    name = ''
    phones = []

    def add_phone(self, obj):
        if isinstance(obj, Phone):
            self.phones.append(obj.phone)

    def edit_phone(self, index, obj):
        if isinstance(obj, Phone):
            self.phones[index] = obj.phone

    def delete_phone(self, obj):
        if isinstance(obj, Phone):
            self.phones.remove(obj.phone)


class Field:
    pass


class AddressBook(UserDict):

    def add_record(self, obj):
        if isinstance(obj, Record):
            self.data[obj.name] = obj.phones