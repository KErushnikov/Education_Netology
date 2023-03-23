import os

counter = 0
for filename in os.listdir("C:\Install"):
    counter = counter + 1
    print(filename)
print('Total:', counter)