import os
from sys import argv
from time import sleep

path = os.popen('path').read().replace("PATH=", '').strip().split(';')

try:
  path.remove(argv[1])
except:
  print(argv[1] + ' Tidak Ditemukan')

path = ';'.join(list(dict.fromkeys(path)))

os.system('setx path "'+path+';"')
os.system('cls')

print('Successfully removed from path')
print('Current user path:')
i = 1
for p in path.split(';'):
  if(p != ''):
    print(str(i) + '. '+p)
    i += 1


sleep(5)
