import random
import string
def rand_num():
    return random.randint(1,10)

s_seed = string.ascii_uppercase + string.digits 
def create_string():
    size=rand_num()
    return ''.join(random.choice(s_seed) for _ in range(size)  )


def create_filename():
    s1 = create_string()
    s2 = create_string()
    name =  s1 + random.choice(file_list) + s2
    return name

file_list = ['glut', 'maya', 'unity']
Filename_Extension = ['.txt', '.jpg', '.png']

Num_Files = 100

name_list=[]
for i in range(Num_Files):
    name_list.append(create_filename())
for i in name_list:
    fp = open(".\\randomFiles\\" + i +random.choice(Filename_Extension), 'w')
    fp.close()