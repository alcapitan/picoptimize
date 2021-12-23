import os
from PIL import Image

def convert_bytes(num):
   for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0
def file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)

print("Pic Optimize  - by Al Capitan")
print("\n")
cwd = os.getcwd() # Localisation path actuel
files = os.listdir(".") # Liste enfants du dossier parent du fichier python
print("In",cwd,"\n")
for i in range(1,len(files)):
	'''img = Image.open(files[i])
	width, height = img.size'''
	files[i] = [files[i]]
	''',width, height]'''
	path = [cwd,files[i][0]]
	path = "/".join(path)
	print("\tName :", files[i][0])
	'''print("\tWidth :", files[i][1])
	print("\tHeight :", files[i][2])'''
	print("\tSize :",file_size(path))
	print("\n")