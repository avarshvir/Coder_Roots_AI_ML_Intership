f = open('file1.txt','a')
f.write(' and I am a CSE student')
f.close()

with open('file1.txt') as f1:
    print(f1.read())
