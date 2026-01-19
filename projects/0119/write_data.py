f = open("C:/Users/405/projects/0119/새파일.txt",'w')
for i in range(1,11):
    data = "%d line of code.\n" % i
    f.write(data)
f.close()
    