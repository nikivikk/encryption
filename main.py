import pyAesCrypt

password = input('Enter the password to encrypt a file: ')

#encrypt
pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)

#decrypt
pyAesCrypt.decryptFile('data.txt.aes', 'dataout.txt', password)