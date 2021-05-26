from collections import UserDict
from datetime import date, datetime
import re


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    # def __init__(self, phone):
    #     self.phone = phone
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if not re.match('^\d{10}', new_value):
            raise ValueError('Phone number must have 10 digits')
        else:
            self.__value = new_value


class Birthday(Field):
    # def __init__(self, birthday=''):
    #     self.birthday = birthday
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if not re.match('\d{2}-\d{2}', new_value):
            raise ValueError('Birthday must be "mm-dd" format')
        b_month, b_day = new_value.split('-')
        if int(b_month) > 12 and int(b_day) > 31:
            raise ValueError('Month must be in "01-12" day must be in "01-31"')
        else:
            self.__value = new_value


class Record:

    def __init__(self, *args):

        self.records = {}
        self.records['phones'] = []
        self.records['birthday'] = ''

        for arg in args:
            if isinstance(arg, Name):
                self.records['name'] = arg.name
            elif isinstance(arg, Phone):
                self.records['phones'].append(arg.value)
            elif isinstance(arg, Birthday):
                self.records['birthday'] = arg.value

    def add_phone(self, obj):
        if isinstance(obj, Phone):
            self.records['phones'].append(obj.value)
            #self.record[self.name] = self.phones

    def edit_phone(self, index, obj):
        if isinstance(obj, Phone):
            self.records['phones'][index] = obj.value

    def delete_phone(self, obj):
        if isinstance(obj, Phone):
            self.records['phones'].remove(obj.value)

    def __count_days(self, d_now, d_birth):
        if d_now > d_birth:
            d_birth = date(d_birth.year + 1, d_birth.month, d_birth.day)
        return d_birth - d_now

    def days_to_birthday(self):
        __birthday = self.records['birthday']
        if __birthday != '':
            result = self.__count_days(datetime.now().date(), date(year=datetime.now().year, month=int(
                __birthday.split('-')[0]), day=int(__birthday.split('-')[1])))
            return f'There are {result.days} days left until the birthday'
        else:
            return f'Sorry, the contact has no date of birth'


class AddressBook(UserDict):

    def __init__(self):
        super(AddressBook, self).__init__()
        self.__record = 0
        self.__record_count = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.__record_count < self.__record:
            result = self.data[self.__record_count]
            self.__record_count += 1
            return result
        else:
            raise StopIteration

    def add_record(self, obj):
        if isinstance(obj, Record):
            self.data[self.__record] = obj.records
            self.__record += 1


if __name__ == '__main__':
    pass


ad = AddressBook()

ph = Phone('0987654321')

bd = Birthday('12-15')

rec = Record(Name("Bob"), ph, bd)

print(rec.days_to_birthday())

ad.add_record(rec)

print(ad)

ph2 = Phone('0987654322')

rec1 = Record(Name('Marley'), ph2)

ad.add_record(rec1)

print(ad)

for rec in ad:
    print(rec)