# import time
# from functools import wraps

# def cache(func):
#     cached_results = {}
    
#     @wraps(func)
#     def wrapper(n):
#         if n not in cached_results:
#             cached_results[n] = func(n)
#             # print("value calculated by function")
#         return cached_results[n]
#     return wrapper
    
# def process_timer(func):
#     @wraps(func)
#     def wrapper(n):
#         start_time =  time.time()
#         result = func(n)
#         end_time = time.time()
#         duration = end_time - start_time
#         wrapper.total_time += (end_time - start_time)

#         return result
#     wrapper.total_time = 0
#     return wrapper

# @process_timer
# @cache
# def factorial_with_cache(n):
#      if n <= 1:
#           return 1
#      return n * factorial_with_cache(n-1)

# @process_timer
# def factorial(n):
#     if n <= 1 :
#         return 1
#     return n * factorial(n-1)

# numbers = [12 , 14 ,32]
# print("cache is :")
# for num in numbers:
#         result = factorial_with_cache(num)
#         print(f"factorial {num}: {result}")
# print("without cache is :")
# for num in numbers:
#         result = factorial(num)
#         print(f"factorial {num}: {result}")

# print (f"with cache : {factorial_with_cache.total_time}")
# print (f"without cache : {factorial.total_time}")
# diff = factorial.total_time - factorial_with_cache.total_time 
# print(f"diffrence is : {diff}")

# --------------------
# class Book:
#     total_books = 0 #class method
#     books = []

#     def __init__(self , title , price):
#         self.title = title
#         self.price = price
#         Book.total_books += 1
        

#     def show(self):
#         print(f"title is : {self.title} , price is : {self.price}")
    
#     @classmethod
#     def total(cls):
#         return cls.total_books
    
# class Bookshop:
#     def __init__(self):
#         self.books = []

#     def add_book(self , book):
#         self.books.append(book)

#     def show_all_books(self):
#         print("book list is :")
#         for book in self.books:
#             book.show()
    
#     def count_books(self):
#         return len(self.books)
    

# bookshop = Bookshop()
# b1 = Book("a" , 1000)
# bookshop.add_book(b1)
# b2 = Book("b" , 2000)
# bookshop.add_book(b2)
# b3 = Book("c" , 3000)
# bookshop.add_book(b3)
# bookshop.show_all_books()
# print(f"all books in bookstore is : {bookshop.count_books()}")
# print(f"all instance is: {Book.total_books}")

# # --------------------
from typing import List , Union
class Person:
    def __init__(self , name , email , gender):
        self.name = name
        self.email = email
        self.gender = gender

    def show_info(self):
        print(f"{self.name} , {self.email} , {self.gender}")

class Auther(Person):
    def __init__(self , name , email , gender , authercode , ganra): 
        super().__init__(name , email , gender) 
        self.authercode = authercode
        self.ganra = ganra

class Poet(Person):
    def __init__(self , name , email , gender , style): 
        super().__init__(name , email , gender) 
        self.style = style

class researcher(Person):
    def __init__(self , name , email , gender , major , university): 
        super().__init__(name , email , gender) 
        self.major = major
        self.university = university


class Puplication:
    count = 0

    def __init__(self , title) : 
        self.title = title
        Puplication.count += 1 

    def get_auther_count(self): 
        raise NotImplementedError("this method should be in child class")
    
class Book(Puplication):
    def __init__(self , title ,  publisher , isbn , authers : Union[Auther , List[Auther]]): 
        super().__init__(title) 
        self.authers = authers if isinstance(authers , List) else [authers]
        self.publisher = publisher
        self.isbn = isbn

    def get_authers_count(self):
        return len(self.authers) 
    
    def __del__(self):
       Puplication.count -= 1

class Article(Puplication):
    def __init__(self , title , year , authers : Union[Auther , List[Auther]]):
        super().__init__(title)
        self.authers = authers if isinstance(authers , List) else [authers]
        self.year = year

    def get_authers_count(self):
        return len(self.authers)
    
class Poetry(Puplication):
    def __init__(self , title , frame):
        super().__init__(title)
        self.frame = frame
        
    def get_authers_count(self):
        return 1


auther1 = Auther("ali" , "a@gmail.com" , "male" , 12 , "scientice")
auther2 = Auther("ati" , "b@gmail.com" , "female" , 18 , "novel")
book1 = Book("a" , "b" , 1000 , auther1)
book2 = Book("c" , "d" , 500 , [auther1 , auther2])

print(f"auther qty for book1: {book1.get_authers_count()}")
print(f"auther qty for book2: {book2.get_authers_count()}")
print(f"total : {Puplication.count}")
del book1
print(f"new total : {Puplication.count}")
    
    











