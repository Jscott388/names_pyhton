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


def names():
    for key, data in users.items():
        print key
        #get count of Student / Instructer and length of the names
        for x in range(len(data)):
            full_name = data[x]["first_name"] +" "+ data[x]['last_name']
            print (x + 1), "-", full_name, "-", (len(full_name)-1)


names()
