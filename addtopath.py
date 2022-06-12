import os
from sys import argv
from time import sleep

path = os.popen('path').read().replace("PATH=", '').strip()
path = path+argv[1]+";"
path = ';'.join(list(dict.fromkeys(path.split(';'))))
os.system(' setx path "'+path+';"')
# os.system('cls')

print('Successfully added to path')
print('Current user path:')
i = 1
for p in path.split(';'):
  if(p != ''):
    print(str(i) + '. '+p)
    i += 1

sleep(5)
