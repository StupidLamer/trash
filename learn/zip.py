import zipfile
import os

folder_path = 'C:\\Users\\grigory\\Desktop\\python\\trash\\learn\\folder'
zip_path = 'C:\\Users\\grigory\\Desktop\\python\\trash\\learn\\folder\\test.zip'
zip_name = 'test.zip'

my_zip = zipfile.ZipFile(zip_path, 'w')

# need_to_zip = 'C:\\Users\\grigory\\Desktop\\python\\trash\\learn\\file.txt'
# my_zip.write(need_to_zip, compress_type=zipfile.ZIP_DEFLATED, arcname='1.txt')

for folder, subfolders, files in os.walk(folder_path):
	print(folder, files)
	for file in files:
		my_zip.write(
			os.path.join(folder, file), 
			os.path.relpath(os.path.join(folder, file)), 
			compress_type=zipfile.ZIP_DEFLATED
			)

my_zip.close()