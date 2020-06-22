import os

message = input("Commit message: ")

os.system('git commit -am "{}"'.format(message))
os.system('git push')
