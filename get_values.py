students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dict(key_name, some_list):
    for some_dict in some_list:
        print(some_dict[key_name])

#we must know the key name in order for this to work
iterate_dict("first_name", students)
iterate_dict("last_name", students)

#searches through keys that are in the dictionary
def iterate_dict2(key_name, some_list):
    for some_dict in some_list:
        if key_name in some_dict:
            print(some_dict[key_name])
        else:
            print(f"Key name: {key_name} is not found!")
#reason for adding else and not found function is so that your funct does not error out, instead it will return a valid piece of code
iterate_dict2("first_name", students)
