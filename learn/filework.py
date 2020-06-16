# f = open('file.txt', encoding='utf-8')
# # text = f.read(2)
# # text2 = f.read(8)
# text3 = f.read()
# f.close()

# print(text3)

# f = open('file.txt', 'a')
# f.write('New string\n' * 2)
# f.close()

# lines = ['New string 1', 'New string 2']
# f = open('file.txt', 'a')
# for i in lines:
# 	f.write(i + '\n')
# f.writelines(lines)
# f.writelines(f'{i}\n' for i in lines)
# f.close()

f = open('file.txt', 'r')
for line in f:
	print(line, end='')
f.close()

