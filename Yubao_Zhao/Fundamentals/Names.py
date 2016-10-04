#Assignment: Names

#Part I
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def print_student_fullname(list):
    for student_dict in list:
        print student_dict['first_name'],student_dict['last_name']
print_student_fullname(students)

#Part II
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def print_user_fullname(dict):
    for user in dict:
        print user
        count = 0
        for name in dict[user]:
            count += 1
            first = name['first_name'].upper()
            last = name['last_name'].upper()
            print "{} - {} {} - {}".format(count, first, last, len(first+last))
print_user_fullname(users)
