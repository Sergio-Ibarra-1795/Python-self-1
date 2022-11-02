import os

current_directory = os.getcwd()

print(current_directory)
contents = os.listdir(current_directory)

print(contents)

print('ice_cream.csv' in contents)