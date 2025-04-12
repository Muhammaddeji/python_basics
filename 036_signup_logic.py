import json 

with open("035_signup_data.json", "r") as file:
    my_list_dict = json.load(file)


    t = input("id")
    i = input("first_name")
    k = input("last_name")
    m = input("email")
    d = input("password")

    data_dict = {
            "id": t,

            "first_name": i,

            "last_name": k,

            "email": m,

            "password": d
            }

    my_list_dict.append(data_dict)

    with open("035_signup_data.json", "w") as file:
        json.dump(my_list_dict, file)

        print("data successfully uploaded to 035_signup_data.json")
