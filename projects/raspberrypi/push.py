import os

message = input("Commit message: ")

os.system('cd OneDrive/Počítač/GIT/PYTHON')
os.system('git commit -am "{}"'.format(message))
os.system('git push')
