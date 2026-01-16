
"""Writing data to text files:
We can write character data to the text files by using the following 2 methods.
write(str)
writelines(list of lines)"""

f=open("abcd.txt",'w')
f.write("Government Polytechnic For Women\n")
f.write("Warangal\n")
f.write("Technical Education\n")
print("Data written to the file successfully")
f.close()