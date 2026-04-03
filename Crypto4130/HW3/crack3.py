from Crypto.Cipher import DES

key = bytes.fromhex("f007ba11ba5eba11")

cipherHex = "64 27 63 80 7a 44 6b 98 3c 2d c9 8f 22 de 55 08 40 29 56 19 48 98 6d 1f 02 2e 03 8a 62 3c b3 bf 51 70d3 2e db cd 93 1b 13 45 e7 a2 0f 16 82 d2 4d 71 55 c3 ff 12 25 38 07 cb 10 c3 80 cf 73 be 6c 22 7d db 55 75 e6 df a5 fb eb 8d ec 81 6f 75 39 de a8 6b 92 cf d4 63 49 10 3d 14 4f 69 f3 2c 52 7f ab 28 cc cb 8c e9"  
ivHex = "191668e63c6d7c45" #not important for ECB

ciphertext = bytes.fromhex(cipherHex.replace(" ", ""))

#ECB is first cypher
cipher = DES.new(key, DES.MODE_ECB)
#print(cipher)
pt = cipher.decrypt(ciphertext)
#print(f"ECB: {pt}")
#ECB: b'\nThe NBA team Utah Jazz actually began as New Orleans Jazz in 1974. This explains their strange name! \n\x01'


#second cypher ??????????????
# cipherHex2 = '69 e7 02 52 7c 08 55 14 ea b6 02 38 e2 64 47 8d 52 da 7d 29 a3 07 71 4b c7 21 94 e7 9b 88 d8 9a 40 4f 41 44 88 e0 b0 42 5b 87 70 7c f1 de 53 39 fb 93 00 5c 2c 0c 36 f6 83 54 42 2d cd 85 6f 26 06 7c 00 03 1a 6d 7a dd 44 bf eb be 58 1e 55 e7 80 d8 57 8f a2 7f db a8'
# ivHex2 = 'f09d673319595818'
# ciphertext2 = bytes.fromhex(cipherHex.replace(" ", ""))
# cipher2 = DES.new(key, DES.MODE_CBC, ivHex2)
# pt2 = cipher2.decrypt(ciphertext)
# print(f"CBC: {pt2}")

#3rd cpyher CBC
cipherHex3 = '05 f3 5d b4 83 26 64 39 cf b4 b4 c0 89 5e 21 94 95 87 c6 ff 0c 00 a9 29 70 fa ef 21 2d b8 2e 70 74 9a98 05 37 6f e0 9d 44 6e 8d 10 20 cc 35 87 61 d9 6e 40 be 29 98 3c 5e bc 4c d5 47 50 18 ca 01 a3 73 fdcc a2 45 52 77 2b e2 86 a1 98 1b 41 0e 16 31 ff f9 dd 47 85 27 1d 72 c9 fc a0 71 1f de 46 ef 88 03 047b 66 82 ac 71 7b ee 35 e0 ea 59 6b a1 d5 e8 fb bb 1f 55 82 2f 6f 81 fa c3 7c dc f5 a2 a5 08 95 b9 8f 9be4 5e eb 7c 96 20 c5 7a 8b bb 26 88 ef 03 80 35 ef f5 79 18 42 3b 16 11 2a 16 28 2b 51 ce bf e1 03 3ce4 c8 35 24 04 93 a0 a5 e1 e8 a4 b9 1d 93 f0 7f d3 61 13 0a cd 64 51 2c 51 32 3b 4d d7 29 cd d6 22 27c9 5f 98 d3 b8 90 24 cc 44 03 b4 8f 5e 10 96 d4 1b ff 8c e3 d9 87 af a7 e9 c2 08 7e 8a 55 bf 6d ea 0e f73c cc 66 6e 59 a8 25 85'
ivHex3= '39db1a2d187e4e3a'
makeSmall = bytes.fromhex(ivHex3)
#print(len(makeSmall))
cipher3 = DES.new(key, DES.MODE_CBC, makeSmall)
ciphertext3 = bytes.fromhex(cipherHex3.replace(" ", ""))
pt3 = cipher3.decrypt(ciphertext3)
print("CBC:", pt3)

## 4th cypher is OFB

