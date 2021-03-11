import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"likes": 10, "name": "Jack", "views": 50},
#         {"likes": 40, "name": "How to tie your shoes", "views": 99},
#         {"likes": 300, "name": "Homemade Pasta", "views": 789}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())

# input()

response = requests.patch(BASE + "video/2", {"views":99, "likes":747})
print(response.json())