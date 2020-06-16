import os

# tree = os.walk('folder')
# for file in tree:
# 	print(file)

def read_dir(folder):
	for root, dirs, files in os.walk(folder):
		level = root.count(os.sep)
		indent = ' ' * 4 * level
		sub_indent = ' ' * 4 * (level+1)
		print(f'{indent}[{os.path.basename(root)}]')
		for i in files:
			print(f'{sub_indent}{i}')

read_dir('folder')