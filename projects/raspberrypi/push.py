import os

message = input("Commit message: ")

os.system('cd /')
os.system('cd Users/matus/OneDrive/Počítač/GIT/PYTHON')
os.system('git commit -am "{}"'.format(message))
os.system('git push')

input('Enter to exit')
