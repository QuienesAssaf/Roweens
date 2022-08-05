#!/usr/bin/env python
import os
os.system ("apt-get install figlet")
os.system ("clear")
os.system("figlet Made By Sikici Roween")
print("""
PORT SIKICI'YE HOSGELDIN!

1: 1.seviye sapla
2: 2.seviye sapla
3: 3.seviye koy icinde kalsın

""")

islemnumara = input('Saplama Hangi Seviyede Olsun?:')

if(islemnumara == "1"):
	HedefIp = input("Hedef IP Gir: ")
	os.system("nmap " + HedefIp)

elif(islemnumara == "2"):
	HedefIp = input("Hedef Ip Gir: ")
	os.system("nmap -sS " + HedefIp)

elif(islemnumara == "3"):
	HedefIp = input("Hedef Ip Gir ")
	os.system("nmap -sS -v " + HedefIp)

else:
	print("Boyle Bir Komut Yok Duzgun Yaz Yarragım ! Yukarıdakilerden Seç: 1, 2, 3,")
