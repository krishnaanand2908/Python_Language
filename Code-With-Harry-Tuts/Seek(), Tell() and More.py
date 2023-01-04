f = open('C:\\Users\\consu\\Desktop\\Krishna Super\\Python_Language\\goodBoy.txt')
print(f.readline())
# print(f.tell())
print(f.seek(10))
print(f.readline())
# print(f.tell())
print(f.seek(0))
print(f.readline())
# print(f.tell())
print(f.seek(0))



f.close()
