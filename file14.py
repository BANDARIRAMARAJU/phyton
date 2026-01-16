# Program to read image file and write to a new image file?
f1=open("sbtet.png","rb")
f2=open("gpw.png","wb")
bytes=f1.read()
f2.write(bytes)
print("New Image is available with the name: newpic.jpg")
