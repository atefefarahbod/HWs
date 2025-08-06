class Student:
    def __init__(self, age: int, height: float, weight: float):
        self.age = age
        self.height = height
        self.weight = weight


class School:
    def __init__(self, name: str):
        self.name = name
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def calculate_average(self):
        total_age = sum(s.age for s in self.students)
        total_height = sum(s.height for s in self.students)
        total_weight = sum(s.weight for s in self.students)
        count = len(self.students)
        return {
            "average_age": round(total_age / count, 2),
            "average_height": round(total_height / count, 2),
            "average_weight": round(total_weight / count, 2),
        }


def compare_schools(school_a: School, school_b: School):
    avg_a = school_a.calculate_average()
    avg_b = school_b.calculate_average()
    print(f"average for school {school_a.name} is {avg_a}")
    print(f"average for school {school_b.name} is {avg_b}")

    if avg_a["average_height"] > avg_b["average_height"]:
        print(f"{school_a.name} is heigher")
    elif avg_b["average_height"] > avg_a["average_height"]:
        print(f"{school_b.name} is heigher")
    else:
        if avg_a["average_weight"] < avg_b["average_weight"]:
            print(f"{school_a.name} is lighter")
        elif avg_b["average_weight"] < avg_a["average_weight"]:
            print(f"{school_b.name} is lighter")
        else:
            print("same result")


def get_school_info(name: str):
    school = School(name)
    n = int(input(f"number of student {name} : "))
    for i in range(1, n + 1):
        age = int(input(f"age for student {i} is :"))
        height = float(input(f"height for student {i} is :"))
        weight = float(input(f"weight for student {i} is :"))
        student = Student(age, height, weight)
        school.add_student(student)
    return school


school_a = get_school_info("A")
school_b = get_school_info("B")
compare_schools(school_a, school_b)
# ----------------
from abc import ABC, abstractmethod


class BaseUser(ABC):
    def __init__(self, name, email):
        pass

    @abstractmethod
    def get_role(self):
        pass


class InvalidEmailError(Exception):
    def __init__(self, email) -> None:
        super().__init__(f"{email} is not valid")


class ValidationMixin:
    def validate_email(self, email):
        if "@" not in email or "." not in email:
            raise InvalidEmailError(email)
        return True


class CustomerUser(BaseUser, ValidationMixin):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.name = name
        self.email = email
        self.validate_email(email)

    def get_role(self):
        return "Customer"


class AdminUser(BaseUser, ValidationMixin):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.name = name
        self.email = email
        self.validate_email(email)

    def get_role(self):
        return "Admin"


info = [
    ("ati", "ati@gmail.com", "admin"),
    ("amir", "amir@gmailcom", "admin"),
    ("farnaz", "farnaz.gmail.com", "customer"),
]
for name, email, role in info:
    try:
        if role == "admin":
            user = AdminUser(name, email)
        else:
            user = CustomerUser(name, email)
        print(f"{user.name} is a {user.get_role()}")
    except InvalidEmailError as e:
        print(e)
