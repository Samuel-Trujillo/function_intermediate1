x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#changing value of 10 NESTED LIST
x[1][0] = 15
print(x)

#Changing last name DICTIONARY INSIDE OF LIST
students[0]['last_name']= 'Bryant'
print(students)

#changing messi LIST INSIDE OF DICTIONARY
sports_directory['soccer'][0]= 'Andres'
print(sports_directory)

#z to 30 DICTIONARY INSIDE OF LIST
z[0]['y']= 30
print(z)