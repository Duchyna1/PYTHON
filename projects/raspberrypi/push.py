import os

message = input("Commit message: ")

print(os.getcwd())
os.system('cd /')
print(os.getcwd())
os.system('cd Users/matus/OneDrive/Počítač/GIT/PYTHON')
print(os.getcwd())
os.system('git commit -am "{}"'.format(message))
os.system('git push')
