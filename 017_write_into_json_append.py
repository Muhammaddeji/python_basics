import json
with open("016_data.json", "r") as my_file:
    my_list = json.load(my_file)


y = input("id:")

u = input("first_name:")

d = input("last_name:")

a = input("email:")

s = input("password:")


data_dict = {

        "id": y,

        "first_name": u,

        "last_name": d,

        "email": a,

        "password": s
        }

my_list.append(data_dict)

print(my_list)

with open("016_data.json", "w") as my_file:
    json.dump(my_list, my_file)
