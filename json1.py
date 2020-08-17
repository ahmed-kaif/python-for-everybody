import json
# importing the json library
# creating a custom json data
data = ''' 
{
        "name" : "kaif",
        "phone": {
            "type" : "intl",
            "number" : "+880 182 101 2388"
        },
        "email" : {
            "hide" : "yes"
        }
}
 '''

info = json.loads(data)  # it creates a list
print('Name:', info["name"])
print('Hide:', info['email']['hide'])
