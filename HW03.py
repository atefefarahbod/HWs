# def find_num(collection):
#     even_num = set()
#     squ = set()

#     def recognize(data):
#         if isinstance(data , (list , tuple)):
#             for item in data:
#                 recognize(item)
#         elif isinstance(data , dict):
#             for value in data.values():
#                 recognize(value)
#         elif isinstance(data , int) and not isinstance(data , bool) and not isinstance(data , str):
#             if data % 2 == 0:
#                 even_num.add(data)
#                 squ.add(data**2)
#     recognize(collection)
#     return even_num , squ

# exp = [1,2,2,4,"ati",[3,4,{"a": [5 ,6] , "b": 6},(7,8,[9,10])]]
# even , squre = find_num(exp)
# print(even)
# print(squre)
# --------------------------
# def find_num(collection):
#     even_num = set()
#     squ = set()
#     saved_num = [collection]
#     while saved_num:
#         current = saved_num.pop()

#         if isinstance(current , (list , tuple)):
#             for item in current:
#                 saved_num.append(item)
#         elif isinstance(current , dict):
#             for value in current.values():
#                 saved_num.append(value)
#         elif isinstance(current , int) and not isinstance(current , bool) and not isinstance(current , str):
#             if current % 2 == 0:
#                 even_num.add(current)
#                 squ.add(current**2)
    
#     return even_num , squ

# exp = [1,2,2,4,"ati",[3,4,{"a": [5 ,6] , "b": 6},(7,8,[9,10])]]
# even , squre = find_num(exp)
# print(even)
# print(squre)
#-------------------------
# def student(student_lst,passing_grade):
#     passed_student = set()
#     failed_student = set()
#     for student in student_lst:
#         if("name" in student and isinstance(student["name"] , str) and "grade" in student and isinstance (student["grade"] , (int,float))):
#             if student["grade"] >= passing_grade:
#                 passed_student.add(student["name"])

#             else:
#                 failed_student.add(student["name"])
#     return(passed_student , failed_student)

# exp = [
#     {"name": "ati" , "grade": 85},
#     {"name": "maryam" , "grade": 59},
#     {"name": "raha" , "grade": 60},
#     {"name": "david" , "grade": "a"},
#     {"name": "ali" },
#     {"grade": 18.5} 
# ]

# passed , failed = student(exp, 60)
# print("passed:", passed)
# print("failed:", failed)
#-------------------------
# def reverse_map(map):
#     result = {}
    
#     for key , value in map.items():
#             if isinstance(key ,str) and isinstance(value ,(list , tuple , set)):
#                 for number in value:
#                     if isinstance(number , int):
#                          if number not in result:
#                             result[number] = set()
#                          result[number].add(key)
                                    
                          
#     return result
    
# exp = {
#     "a":[1,2,3],
#     "b":[2,3],
#     "c":[3,"x"],
#     5:[1,2],
#     "d":"hello"
# }

# final = reverse_map(exp)
# print(final)
#-------------------------
# def inventory(input_file , output_file , final):
#     inventory = {}

#     with open("./text.txt" , "r" , encoding="utf-8") as f:
#         next(f)
#         for line in f:
#             line = line.strip()
#             if not line:
#                 continue
#             parts = line.split(",")
#             if len(parts) != 3:
#                 continue
            
#             quantity , item , operation = parts
#             try:
#                 quantity = int(quantity)
#             except ValueError:
#                 continue
           
#             if operation in ("add" , "plus"):
#                 inventory[item] = inventory.get(item,0) + quantity
#             elif operation == "remove":
#                 inventory[item] = inventory.get(item,0) - quantity
#         filtered_items =[item for item,qty in inventory.items() if qty >= final]
#         filtered_items.sort()
#         with open("./text2.txt" , "w" , encoding= "utf-8") as f:
#             for item in filtered_items:
#                 f.write(f"{item}\n")

# inventory("./text.txt" ,"./text2.txt" , 5)
#-------------------------
a = input("inser something : ").split(" ")
dict1 ={}
for i in a:
    i = i.lower().strip()
    if  i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print("word , count")       
for i, count in dict1.items():
    print(f"{i},{count}")
#-------------------------
# password = "@li" 
# username = "ali"
# user_input = "ALI"
# input_pass = "aLi"

# if password == input_pass.lower().replace("a","@").replace("A","@").replace("s","$"):
#     print("hello")
# txt = "hi{name}"
# print(txt.format(name = "ali"))
# num = 50
# print(f"{num : .2f}")
# print(f"{num : 010d}")



