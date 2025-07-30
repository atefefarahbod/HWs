class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def __str__(self):
        return f" Dr. {self.name} , specialty is :{self.specialty}"


class Patient:
    def __init__(self, name, age, history):
        self.__name = name
        self.__age = age
        self.__history = history if isinstance(history , list) else []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) >= 2:
            self.__name = value
        else:
            raise ValueError("name error")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0 and value < 120:
            self.__age = value
        else:
            raise ValueError("age error")

    @property
    def history(self):
        return self.__history

    def add_history(self, new):
        if isinstance(new, str):
            self.__history.append(new)
        else:
            raise ValueError("history error")

    def __str__(self):
        return f"{self.name} , age: {self.__age} , history : {",".join(self.__history)}"


from datetime import datetime


class Appointment:
    def __init__(self, doctor, paitent, date_time):
        self.doctor = doctor
        self.paitent = paitent
        self.date_time = date_time

    def __str__(self):
        return f"{self.paitent.name} has an appointment in {self.date_time.strftime("%Y-%m-%d %H:%M")} with {self.doctor.name}"


class Clinic:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def show_appointment(self):
        if not self.appointments:
            print("no appointment")
        for appointment in self.appointments:
            print(appointment)

    def appointment_for_doctor(self, doctor_name):
        results = [
            appointment
            for appointment in self.appointments
            if appointment.doctor.name == doctor_name
        ]
        if not results:
            print(f"{doctor_name} has no appointment")
        else:
            for appointment in results:
                print(appointment)


dr1 = Doctor("a" , "ghalb")
dr2 = Doctor("b" , "neuro")
pa1 = Patient("aa" , 18 , ["bimarighalbi"])
pa2 = Patient("bb" , 52 , ["bimarimaghzi"])
pa3 = Patient("cc" , 32 , ["kamardard"])
pa1.add_history("tashanoj")
print(pa1)
app1 = Appointment(dr1 , pa1 , datetime(2025, 8, 2, 10, 30))
app2 = Appointment(dr2 , pa2 , datetime(2025, 8, 2, 11, 0))
app3 = Appointment(dr1 , pa3 , datetime(2025, 8, 2, 11, 30))
clinic = Clinic()
clinic.add_appointment(app1)
clinic.add_appointment(app2)
clinic.add_appointment(app3)
clinic.show_appointment()
clinic.appointment_for_doctor("a")

# ----------------------------
from datetime import date
class Person:
    def __init__(self , firt_name , last_name , birth_date , national_id):
        self.firt_name = firt_name
        self.__last_name = last_name
        self.__birth_date = birth_date
        self.__national_id = national_id

    def show_national_id(self , masked = True):
        if masked:
            return "*" * (len(self.__national_id) - 4) + self.__national_id[-4:]
        else:
            return self.__national_id
        
    @property
    def age(self):
        today = date.today()
        age = today.year - self.__birth_date.year
        if (today.month , today.day) < (self.__birth_date.month , self.__birth_date.day):
            age -= 1
        return age
    
    @property
    def is_adult(self):
        return self.age >= 18
    
    def update_last_name(self , new):
        if new.strip():
            self.__last_name = new
        else:
            raise ValueError("please fill new last name")
        
    def change_birth_date(self , new_date):
        today = date.today()
        max_of_date = date(today.year - 80 , today.month , today.day)
        if new_date >= max_of_date:
            self.__birth_date = new_date
        else:
            print("too old")
        
    def __str__(self):
        return f"{self.firt_name} , {self.__last_name} , age: {self.age} , adult: {self.is_adult}"
    
p1 = Person("atefe" , "farahbod" , date(1985, 1, 15) , "1214328545")
print(p1)
print(p1.age)
print(p1.is_adult)
print(p1.show_national_id())
print(p1.show_national_id(masked=False))
p1.update_last_name("lilian")
print(p1)
p1.change_birth_date(date(1800, 1, 1))
#---------------------------------
from math import gcd
class Fraction:
    def __init__(self , numerator , denominator):
        if denominator == 0:
            raise ValueError("zero is not valid num")
        
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        
        normal = gcd(numerator , denominator)
        self.numerator = numerator // normal
        self.denominator = denominator // normal

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self , other):
        a = self.numerator * other.denominator + other.numerator * self.denominator
        b = self.denominator * other.denominator
        return Fraction(a , b)
    
    def __sub__(self , other):
        a = self.numerator * other.denominator - other.numerator * self.denominator
        b = self.denominator * other.denominator
        return Fraction(a , b)
    
    def __mul__(self , other):
        a = self.numerator * other.numerator
        b = self.denominator * other.denominator
        return Fraction(a , b)

    def __truediv__(self , other):
        if other.numerator == 0 :
            raise ZeroDivisionError("zero")
        a = self.numerator * other.denominator
        b = self.denominator * other.numerator
        return Fraction(a , b)
    
    def __eq__(self , other):
        return self.numerator * other.denominator == self.denominator * other.numerator
    
    def __ne__(self , other):
        return not self == other
    
    def __lt__(self , other):
        return self.numerator * other.denominator < self.denominator * other.numerator
    
    def __le__(self , other):
        return self.numerator * other.denominator <= self.denominator * other.numerator
    
    def __gt__(self , other):
        return self.numerator * other.denominator > self.denominator * other.numerator
    
    def __ge__(self , other):
        return self.numerator * other.denominator >= self.denominator * other.numerator
    
f1 = Fraction(1 , 2)
f2 = Fraction(3 , 4)

print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)

print(f1 < f2)
print(f1 == Fraction(2,4))
print(f1 != f2)
#---------------------------------
class Engine:
    def __init__(self , horsepower , fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type

    def engine_info(self):
        return f"{self.horsepower} , {self.fuel_type}"
    
class Vehicle:
    def __init__(self , make , model , year , engine: Engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine

    def vehicle_info(self):
        return f"{self.make} , {self.model} , {self.year} ,{self.engine.engine_info()}"
    
    def __str__(self):
        return self.vehicle_info()
        
class Car(Vehicle):
    def __init__(self, make, model, year, engine, num_doors):
        super().__init__(make, model, year, engine)
        self.num_doors = num_doors

    def vehicle_info(self):
        return super().vehicle_info() + f"{self.num_doors}"
    
class Truck(Vehicle):
    def __init__(self, make, model, year, engine, playload_capacity):
        super().__init__(make, model, year, engine)
        self.playload_capacity = playload_capacity

    def can_carry(self , weight):
        return weight <= self.playload_capacity
    
    def vehicle_info(self):
        return super().vehicle_info() + f"{self.playload_capacity}"
    
class ElectricCar(Car):
    def __init__(self, make, model, year, horsepower, num_doors):
        engine = Engine(horsepower , "electric")
        super().__init__(make, model, year, engine, num_doors)


class GasCar(Car):
    def __init__(self, make, model, year, horsepower, num_doors):
        engine = Engine(horsepower , "Gas")
        super().__init__(make, model, year, engine, num_doors)

class Garage:
    def __init__(self) -> None:
        self.vehicles = []

    def add_vehicle(self , vehicle):
        self.vehicles.append(vehicle)

    def list_vehicle(self):
        for x in self.vehicles:
            print(x)

    def sort_by_year(self , desc=False):
        self.vehicles.sort(key=lambda x: x.year , reverse=desc)

    def sort_by_horsepower(self , desc=False):
        self.vehicles.sort(key=lambda x: x.engine.horsepower , reverse=desc)

e1 = Engine(150 , "petrol")
e2 = Engine(300 , "diesel")

c1 = Car("toyota" , "corolla" , 2022 , e1, 4)
c2 = Car("peugeot" , "206" , 2018 , e1, 4)
t1 = Truck("volvo" , "FH" , 2021 , e2, 12000)

print(c1)
print(t1.can_carry(13000))

garage = Garage()
garage.add_vehicle(c1)
garage.add_vehicle(c2)
garage.add_vehicle(t1)

garage.sort_by_year(desc=True)
garage.list_vehicle()
print("____")
garage.sort_by_horsepower()
garage.list_vehicle()
