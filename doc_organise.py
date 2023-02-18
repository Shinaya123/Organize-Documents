import os
import shutil

from_dir= "C:/Users/manak/Downloads"
to_dir= "C:/Users/manak/Downloads/test2"
list_of_files=os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    root, extension=os.path.splitext(file_name)
    #print(name)
    #print(extension)
    if extension=='':
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1= from_dir + '/' + file_name
        path2= to_dir + '/' + 'Image_Files'
        path3= to_dir + '/' + 'Image_Files' + file_name
      # print("path1", path1)
       #print("path3", path3) 
        if os.path.exists(path2):
            print('moving'+ file_name + '.....')
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print('moving'+ file_name + '.....')
            shutil.move(path1, path3)