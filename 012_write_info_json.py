student = {
        
        "id":        "009",
        
        "name":      "Adedeji",
        
        "gender":    "Male",

        "department": "arts",

        "school":     "unilorin"
        }

import json

with open("013_data.json", "w") as my_file:
    json.dump(student, my_file)

print(student)
