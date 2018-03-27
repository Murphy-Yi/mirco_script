import os

path = '/Users/zhangyi/Desktop/项目'
files = os.listdir(path)
file = ''
for i in files :
    if file in i and i.endswith('.jpeg'):
        print("Found it!"+ str(i))