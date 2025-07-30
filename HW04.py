# users = [
#     {
#         "username" : "ali",
#         "posts": [
#             {"likes" : 12 , "shares" : 5},
#             {"likes" : 30 , "shares" : 1},
#             {"likes" : 15 , "shares" : 0}
#         ],
#         "friends" : {"sara" , "mina" , "hamid"}
#     },
#     {
#         "username" : "sara",
#         "posts": [
#             {"likes" : 22 , "shares" : 1},
#             {"likes" : 6 , "shares" : 2}
#         ],
#         "friends" : {"ali" , "hamid"}
#     },
#     {
#         "username" : "mina",
#         "posts": [
#             {"likes" : 5 , "shares" : 1}
#         ],
#         "friends" : {"ali"}
#     }
# ]
# max_total = 0
# top_user = None
# for user in users:
#     likes = 0
#     shares = 0
#     total = 0
#     for post in user["posts"]:
#         likes += post["likes"]
#         shares += post["shares"]
#         total += (post["likes"]+post["shares"])
#         if total > max_total:
#             max_total = total 
#             top_user = user["username"]

#     print(f"user: {user["username"]}")
#     print(f"likes: {likes}")
#     print(f"share: {shares}")
#     print(f"total : {likes+shares}")
# print(f"top_user : {top_user} with :{max_total}")

# friends_count_dict = {}
# for user in users:
#     num_friends = len(user["friends"])
#     if num_friends not in friends_count_dict:
#         friends_count_dict[num_friends] = []
#     friends_count_dict[num_friends].append(user["username"])
# print(friends_count_dict)

# if_1 = lambda user : len(user["posts"]) >= 2
# if_2 = lambda user : any(post["likes"] > 20 for post in user["posts"])
# filtered_user = [user["username"] for user in users if if_1(user) and if_2(user)]
# print(filtered_user)
# # a = len(users[2]["posts"])
# # print(a)

# user_rate = []
# for user in users:
#     total_likes = sum(post["likes"] for post in user["posts"])
#     total_shares = sum(post["shares"] for post in user["posts"])
#     friend_count = len(user["friends"])
#     total_rate = (total_likes + total_shares) / friend_count if friend_count != 0 else 0
#     user_rate.append((user["username"] , total_rate))
# user_rate_sorted = sorted(user_rate , key = lambda x : x[1] , reverse=True)
# top_3_user = user_rate_sorted[:3]
# print("top__users:")
# for user,rate in top_3_user: 
#     print(f"{user} : ratio {rate:.2f}")

#-------------------------
# def number_generator():
#     import random
#     while True:
#         yield random.randint(0,10000000)

# def process_number():
#     seen = set() # repeated nums
#     qualified = [] # up to 50 nums
#     max_7_num = None
#     max_7_count = -1
#     for num in number_generator():
#         if num in seen:
#             continue
#         seen.add(num)

#         num_str = str(abs(num))
#         digit_count = len(num_str)
#         digit_sum = sum(int(d) for d in num_str)

#         if digit_count % 2 == 1 and digit_sum >= 5:
#             qualified.append(num)

#             seven_count = num_str.count('7')
#             if seven_count > max_7_count:
#                 max_7_count = seven_count
#                 max_7_num = num
#             elif seven_count == max_7_count:
#                 if num > max_7_num:
#                  max_7_num = num
            
#         if len(qualified) == 50:
#             break
#     return qualified , max_7_count , max_7_num
    
# qualified_nums , max_7s_count , num_with_most_7s = process_number()
# print(qualified_nums)
# print(max_7s_count)
# print(num_with_most_7s)
#-------------------
raw_scores = [
    "ali:match-17;physics-18.5;chemestry-15",
    "sara:match-20;physics-19;chemestry-19.5",
    "reza:match-16;physics-14.5;chemestry-13",
    "zahra:match-18.5;physics-20;chemestry-20",
]

extract_scores = lambda student: list(map(lambda x: x.split("-"), student.split(":")[1].split(";")))
all_score = list(map(extract_scores,raw_scores))
subject_scores = {}
for student in all_score:
    for subject , score in student:
        subject_scores.setdefault(subject , []).append(float(score))  
result = []
for subject , scores in subject_scores.items():
    average = sum(scores) / len(scores)
    result.append((subject,average))
for subject , avg in result:
    print(f"'{subject}' : {avg}")



    

