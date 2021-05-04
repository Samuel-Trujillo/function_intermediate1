dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(some_dict):
    #this is used to loop through dictionary
    for key in some_dict:
        print(f"{len(some_dict[key])} {key.upper()}")
        for item in some_dict[key]:
            print(item)
        #makes a space in the output 
        print()

print_info(dojo)
