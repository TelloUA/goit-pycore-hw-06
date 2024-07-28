from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        self._validate(value)
        super().__init__(value)

    def _validate(self, value):
        if len(value) != 10:
            raise Exception("Number must be 10 digits")

    def set_value(self, value):
        self._validate(value)
        self.value = value

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self, phone: str):
        field = Phone(phone)
        self.phones.append(field)

    def remove_phone(self, phone: str):
        self.phones = [field for field in self.phones if field.value != phone]

    def edit_phone(self, old_phone: str, new_phone: str):
        finded = [field for field in self.phones if field.value == old_phone]
        for item in finded:
            item.set_value(new_phone)

    def find_phone(self, phone: str):
        finded = [field for field in self.phones if field.value == phone]
        return finded[0] if len(finded) else None

class AddressBook(UserDict):
    # реалізація класу
    def add_record(self, record: Record):
        self.data.update({record.name.value : record})

    def find(self, name: str):
        return self.data.get(name)

    def delete(self, name: str):
        if name in self.data:
            self.data.pop(name)
