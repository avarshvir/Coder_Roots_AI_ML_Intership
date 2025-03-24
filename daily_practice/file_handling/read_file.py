f = open('file1.txt','r')
print(f.read())

f.close()

with open('file1.txt','r') as f1:
    print(f1.read())