# ------------------------------------------------------------------------------------------------
#    LIBRERIAS os, glob y sys
# ------------------------------------------------------------------------------------------------

import os, glob, sys

print("os.name: ", os.name)                 # posix   (unix)
# print(os.getuid())            		    # 3360    (usuario)
print("os.getpid(): ", os.getpid())  		# 3360    (usuario)
print("os.getcwd(): ", os.getcwd())			# (dir. actual)

# sys.version_info(major=2, minor=7, micro=3, releaselevel='final', serial=0)
print("sys.version_info: ", sys.version_info)
# ['script.py']  (lista con los archivos en directorio)
print("glob.glob('*.*'): ", glob.glob('*.*'))


path = "D:\Python\Librerias\os"
 
for (path, dirs, files) in os.walk(path):
    print("----")			# ----
    print(path)				# /home/run2359
    print(dirs)				# []
    print(files)			# ['script.py']