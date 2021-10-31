def change():
   
   file1="/users/shivanshu/desktop/python/gessgame/file1"
   file2="/users/shivanshu/desktop/python/gessgame/file"
   with open(file1,'r') as a:
       data_a = a.read()
   with open(file2,'r') as a:
       data_b = b.read()
   with open(file1,'w') as a:
       a.write(data_b)
   with open(file2,'w') as a:
       b.write(data_a)
change()