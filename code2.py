f = open('text2.txt','r')
data = f.readlines()
f.close()

data.insert(0,' Hallo Anas \n')
print(data)


f2 = open('text2.txt','w') #python append to file
f2.write('\n'.join(data))
f2.close()

