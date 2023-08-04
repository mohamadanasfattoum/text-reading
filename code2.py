f = open('text2.txt','r')
data = f.readlines()
f.close()

data.insert(0,'\n Hallo Anas  ')



f2 = open('text2.txt','a') #python append to file
f2.write('\n'.join(data))
f2.close()

