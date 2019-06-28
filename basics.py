my_dict = {}

my_dict['name'] = 'sharaf'
my_dict['place'] = 'india'
my_dict['age'] = 25

print my_dict


my_dict['name'] = 'noob'

print my_dict

del my_dict['name']

print my_dict

for k, v in my_dict.iteritems():
    print k
    print v
