import os
from sys import argv
from time import sleep

path = os.popen('reg query HKEY_CURRENT_USER\Environment /v path').read(
).replace("""HKEY_CURRENT_USER\Environment
    path    REG_SZ    """, '').strip().split(';')
path.remove(argv[1])
path = ';'.join(list(dict.fromkeys(path)))

os.system('setx path "'+path+'"')
os.system('cls')

print('Telah dihapus dari path')
print('User Path Sekarang:')
i = 1
for p in path.split(';'):
  if(p != ''):
    print(str(i) + '. '+p)
    i += 1


sleep(5)
