# def sed (file_input , file_output , patern_string , replacement_string):
#   try:
#     with open("./file_input.txt" , "rt") as fin , open("./file_output.txt" , "wt") as fout:
#       for line in fin:
#         new_line = line.replace(patern_string , replacement_string)
#         fout.write(new_line)
#   except FileNotFoundError as fnf_err:
#         print(f"FileNotFindError : {fnf_err}")
#   except TypeError as type_err:
#         print(f"TypeError : {type_err}")
#   except Exception as e:
#         print(f"unexpected error : {e}")
              

# sed("file_input","file_output" , "hello" , "hi")     

# import os
# print(os.listdir())
# -----------------test2
# student_name = input("plese insert your first name and your last name: ") or "not entered"
# phone = input("plese insert your phone number: ") or "not entered"
# email = input("plese insert your email: ") or "not entered"
# try:
#       with open ("./contacts.txt","at", encoding = "UTF-8") as contacts:
#             contacts.write(f"file contacts\n name :{student_name}\n phone :{phone}\n email :{email}\n encoding UTF8\n")
#       print("cantact saved successfully in contacts.txt")
#       with open ("./contacts.txt","rt", encoding = "UTF-8") as contacts:
#             print(contacts.read())
# except Exception as e:
#       print(f"error on save ,{e}")
# # ----------------test3
# import statistics
# def analyze_data(*args , oper = "average"):
#       print(type(args))
#       try:
#            numbers = [float(num) for num in args]
#            if oper == "sum":
#                   return ("sum" ,sum(numbers))
#            if oper == "average":
#                   return ("average" , statistics.mean(numbers))
#            elif oper == "max":
#                   return ("max" , max(numbers))
#            else:
#                   return "Invalid operator"
#       except ValueError:
#             return "All inputs must be numbers"

# print(analyze_data(12, 13, 14, 15, 16, oper="sum"))      
# print(analyze_data(12, 13, 14, 15, oper="average"))  
# print(analyze_data(14, 15, 16,17, oper="max"))

# ----------------tesr 4 ok
# def analyze_log_file():
#     total = 0
#     info = 0
#     warning = 0
#     error = 0

#     try:
#         with open("./server.log.txt", "r") as file:
#             for line in file:
#                 total += 1
#                 if "INFO" in line:
#                     info += 1
#                 elif "WARNING" in line:
#                     warning += 1
#                 elif "ERROR" in line:
#                     error += 1
#     except FileNotFoundError:
#         print("file not found")
        

#     return (total, info, warning, error)  



# total, info, warning, error = analyze_log_file()

# info_percent = (info / total) * 100
# warning_percent = (warning / total) * 100
# error_percent = (error / total) * 100


# with open("report.txt", "w") as report:
#     report.write("=== Server Log Analysis Report ===\n")
#     report.write(f"Total entries: {total}\n")
#     report.write(f"INFO: {info}\n")
#     report.write(f"WARNING: {warning}\n")
#     report.write(f"ERROR: {error}\n")

#     report.write(f"INFO percent: {info_percent}%\n")
#     report.write(f"WARNING percent: {warning_percent}%\n")
#     report.write(f"ERROR percent: {error_percent}%\n")
# ----------------test 5
# def calculate(num1, num2, operator='+'):
#     try:
#         num1 = float(num1)
#         num2 = float(num2)

#         if operator == '+':
#             return num1 + num2
#         elif operator == '-':
#             return num1 - num2
#         elif operator == '*':
#             return num1 * num2
#         elif operator == '/':
#             return num1 / num2
#         else:
#             return "Invalid operator"
#     except ValueError:
#         return "Invalid number"
#     except ZeroDivisionError:
#         return "Cannot divide by zero"

# print(calculate(10,20))
# print(calculate(10,20,"+"))
# print(calculate(10,20,"-"))
# print(calculate(10,20,"*"))
# print(calculate(10,0,"/"))
