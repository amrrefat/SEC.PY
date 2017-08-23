import hashlib
from platform import system
import os , sys

if system() == 'Linux':
    os.system('clear')
elif system() == 'Windows':
    os.system('cls')
print ('''
[*] To know the type of Hash

  ██████ ▓█████  ▄████▄        ██▓███  ▓██   ██▓
▒██    ▒ ▓█   ▀ ▒██▀ ▀█       ▓██░  ██▒ ▒██  ██▒
░ ▓██▄   ▒███   ▒▓█    ▄      ▓██░ ██▓▒  ▒██ ██░
  ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒     ▒██▄█▓▒ ▒  ░ ▐██▓░
▒██████▒▒░▒████▒▒ ▓███▀ ░ ██▓ ▒██▒ ░  ░  ░ ██▒▓░
▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░ ▒▓▒ ▒▓▒░ ░  ░   ██▒▒▒ 
░ ░▒  ░ ░ ░ ░  ░  ░  ▒    ░▒  ░▒ ░      ▓██ ░▒░ 
░  ░  ░     ░   ░         ░   ░░        ▒ ▒ ░░  
      ░     ░  ░░ ░        ░            ░ ░     
                ░          ░            ░ ░     


''')

while True:
    the_hash = input ('[*]enter the hash > ')
    if int(len(the_hash))==32:
        print ('[+] hash >>> MD5' + ' or ' + 'MD4')
    elif int (len (the_hash)) ==40:
        print ('[+] hash >>> SHA1' +' or ' + 'ecdsa-with-SHA1' + ' or ' +' DSA-SHA  or ripemd160')
    elif int (len (the_hash)) == 56 :
        print ('[+] hash >>> SHA224')
    elif int(len(the_hash)) == 64:
        print ("[+]HASH >> SHA256 ")
    elif int(len(the_hash)) == 96:
        print ("[+]HASH >> SHA384 HASH or sha384")
    elif int(len(the_hash))== 128:
        print ("[+]hash >> SHA512 or sha512")
    elif int(len(the_hash))== 130:
        print ('[*] hash >> whirlpool')
    else:
        print ('[#]error >> not found ')
        
