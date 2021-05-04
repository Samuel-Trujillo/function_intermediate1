students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

#good for if you know the key names
def interate_dictionary(some_list):
    #loop thru list
    for item in some_list:
        print(f"first_name - {item['first_name']}, last_name - {item['last_name']}")


#better version for when you dont know the key names
def iterate_dictionary2(some_list):
    print_string =""
    for item in some_list:
        for key, value in item.items():
            print_string += f"{key} - {value}, "
        print(print_string)
        print_string = ""

iterate_dictionary2(students)
