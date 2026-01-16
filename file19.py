#Q1. To Know Current Working Directory:
import os
cwd=os.getcwd()
print("Current Working Directory:",cwd)
# Q2. To create a sub directory in the current working directory:
import os
os.mkdir("mysub")
print("mysub directory created in cwd")
