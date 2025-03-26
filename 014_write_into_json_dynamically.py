import json

d = input("user id:")

q = input("user first_name:")

h = input("user last_name:")

o = input("user email:")

p = input("user password:")


user = {
        
        "id": d,
        
        "first_name": q,

        "last_name":  h,

        "email": o,

        "password": p
        }

with open("015_register.json", "w") as my_file:
    json.dump(user, my_file)

print(user)
