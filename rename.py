import sys
import os

id = '06160485'
fileList = []
for file in sys.argv:
    fileList.append(file)
    
for file in fileList[1:]:
    if file.find(id) == -1:
        t_filename = os.path.split(file)
        dst = t_filename[0] + '\\' + id + t_filename[1]
        os.rename(file,dst)
        print(dst)

input("press any key to quit.")
   

