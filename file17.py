from zipfile import *
f=ZipFile("files.zip",'w',ZIP_DEFLATED)
f.write("abcd.txt")
f.write("ab.txt")
f.write("abc.txt")
f.close()
print("files.zip file created successfully")
