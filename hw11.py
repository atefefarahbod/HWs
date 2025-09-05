# import requests
# import json

# class MovieAddress:
#     def __init__(self , url):
#         self.url = url
#         self.session = None
        
#     def __enter__(self):
#         self.session = requests.Session()
#         print("connection is now available")
#         return self
    
#     def __exit__(self , exc_type , exc_val , exc_tb):
#         self.session.close()
#         print("connection is now close")
        
#     def get_movies(self):
#         url = f"{self.url}/movies"
#         response = self.session.get(url)
#         if response.status_code == 200:
#             movies = response.json()
#             for movie in movies:
#                 print(f"{movie["Title"]}({movie["Year"]})")
#         else:
#             print("can not get movie info")
            
#     def add_movie(self , title , year , runtime , poster):
#         url = f"{self.url}/movies"
#         data = {"Title":title ,
#                 "Year": year,
#                 "Runtime": runtime,
#                 "Poster": poster
#                 }
#         response = self.session.post(url , json=data)
        
#         if response.status_code == 201:
#             print(f"movie {title} add successfuly")
#         else:
#             print(f"error in add movie {response.status_code}")
            
            
# url = "http://my-json-server.typicode.com/horizon-code-academy/fake-movies-api"
# with MovieAddress(url) as api:
#     api.get_movies()
#     api.add_movie("lionking" , "2019", "118 min","https://www.amazon.com.au/Jefuzh-Mufasa-Posters-Bedroom-Unframed/dp/B0DNCKPSGZ")
# ---------------------------------------------------------------------------
"""JSON is more compact and can be easily loaded in JavaScript.
XML is stricter and has support for schemas and namespaces.
On the face of it JSON seems superior in every way - it's flexible, more compact and in many cases easier to use (especially when working with JavaScript), however it lacks some key features, in particular:

Schema support

I.e. the ability for party A to specify the format of a document, and the ability for party B to check that they are supplying something that matches this format.

This is crucial when passing data between separate systems, where a deviation from the expected format might mean that the data cannot be processed (or worse, is processed incorrectly).

Namespace support

I.e. the ability to mix data intended to be read by multiple sources (or written by multiple sources) in the same document.

An example of this in action is the SOAP protocol - namespaces allow for the separation of the SOAP "Envelope", or "Wrapper" data which is passed alongside the serialised application data. This allows web frameworks process and handle the SOAP Envelope and then pass the body / payload data onto the application.

JSON is very useful when developing a web application where fast, compact and convenient serialisation of data is required, however it's flexible nature is the very thing that makes it less suitable than XML for transferring data between separate systems, or storing data that will be read by 3rd parties."""

# ------------------------------------
import requests
import logging
from datetime import datetime

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s " , 
    filename = "sports.log",
    filemode = "a"
)

class Varzeshkar:
    def __init__(self , name , age , city) -> None:
        self.name = name
        self.age = age
        self.city = city
        self.activities = []
        
    def add_activity(self , type , distance , date , time , weather):
        weather = weather.get_weather(self.city)
        if weather is None:
            logging.error("error in getting info from weather")
            print("can not reach to weather")
            return
        
        if type.lower() == "run" and "rain" in weather.lower():
            logging.warning(f"{self.name} wants to run in rainy weather")
            print("warning: weather is rainy")
            
        activity = {"type" : type,
                    "distance" : distance,
                    "date" : date,
                    "time" : time 
                    }
        self.activities.append(activity)
        logging.info(f"new activity saved for{self.name} as {type} , {distance}")
        print(f"activity saved {type} , {distance}")
        
    def show_activities(self):
        print(f"{self.name}")
        for i in self.activities:
            print(f"{i["type"]} , {i["distance"]}, {i["date"]} , {i["time"]}")
    
class Weather:
    def __init__(self , api) -> None:
        self.api = api
        
    def get_weather(self , city):
        try:
            url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={self.api}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data["weather"][0]["description"]
            else:
                return None
        except Exception as e:
            logging.error(f"api error{e}")
            
api = "https://openweathermap.org/city"
weather = Weather(api)
varzeshkar = Varzeshkar("ati" , 40 , "Losangeles")
today = datetime.now().strftime("%Y-%m-%d")
time_now = datetime.now().strftime("%H:%M")


varzeshkar.add_activity("run" , 5 , today , time_now , weather)
varzeshkar.add_activity("swim" , 2 , today , time_now , weather)
varzeshkar.show_activities()
        
        
        
        