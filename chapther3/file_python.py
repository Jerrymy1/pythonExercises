#import pathlib
from pathlib import Path
'''path = pathlib.Path("C:/Cohort14/private.img")
print(path.is_absolute())



path = pathlib.Path("C:\kelloges\hello.txt")
print(path)'''


#path = pathlib.Path("Cohort14/private.img")
path = Path("/Cohort14/private.img")
#cwd_path = pathlib.Path.cwd()
cwd_path = Path.cwd()/"Jerry" / "numbers" / "green.csv"
print(cwd_path)
'''
#print("Parent -", cwd_path.parent)
print("Parent -", path.parent)
#print(list(cwd_path.parents))
print (list(path.parents))
print("Anchor - ", path.anchor)
print("Name - ", path.name)
print("Suffix - ", path.suffix)
print("Stem - ", path.stem)

cwd_path.mkdir(exist_ok=True)
new_file_path = cwd_path / "private.txt"
new_file_path.touch()
print(path.exists())
print(cwd_path.exists())
print(cwd_path.exists())
'''

cwd_path.parent.mkdir()




