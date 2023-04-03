from dataclasses import dataclass

def get_first_name(self):
    return self.first_name


def get_last_name(self):
    return self.last_name


def get_middle_name(self):
    return self.middle_name

def init(self, first_name, last_name, middle_name):
    self.first_name = first_name
    self.last_name = last_name
    self.middle_name = middle_name


class BaseUser:
    def __str__(self):
        return "<user-object>"


attrs = {
    "first_name" : "",
    "last_name" : "",
    "middle_name" : "",
    "get_first_name" : get_first_name,
    "get_last_name" : get_last_name,
    "get_middle_name" : get_middle_name,
    "__init__": init
}

bases = (
    BaseUser,
)


class Meta(type):

    def __new__(cls, name, bases, attrs):
        print("new")
        fields = dict()
        for key in attrs["__annotations__"].keys():
            fields[key] = ""
        print(attrs["__annotations__"])
        attrs["fields"] = fields
        return super().__new__(cls, name, bases, attrs)


@dataclass
class Data(metaclass=Meta):
    id:  int
    name: str
    email: str

    def row(self) -> tuple:
        return str(self.id), self.name, self.email


#print(Data.__dict__.get("__dataclass_fields__"))

User = type("User", bases, attrs)
user1 = User("John", "Test", "Tel00v14")

print(str(user1))
print(user1.get_first_name())
print(user1.get_last_name())
print(user1.get_middle_name())
