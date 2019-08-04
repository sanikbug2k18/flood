import os
import sys
from core.starkmcore import *

def deepstore():
 print(colored("""
     ==================================================
	   
	     ____
         /\  _`\
         \ \ \/\ \     __      __    _____
          \ \ \ \ \  /'__`\  /'__`\ /\ '__`\
           \ \ \_\ \/\  __/ /\  __/ \ \ \L\ \
            \ \____/\ \____\\ \____\ \ \ ,__/
             \/___/  \/____/ \/____/  \ \ \/
                                       \ \_\
                                        \/_/
 
     ==================================================
        1. My Blogger
        2. A Story (in progress)
        3. Phishing Websites (sites in search)
        4. Video on Termux Channels
        5. Play YouTube songs
     ==================================================
        6. log out
     ==================================================
        """, 'red'))

 deep = raw_input("BUG > ")

 if deep == "1":
     blog()
 elif deep == "4":
 	os.system("clear")
        Youtube()
 elif deep == "3":
 	fish()
 elif deep == "5":
 	os.system("mpsyt")
 elif deep == "6":
     os.system("clear")
     restartprogram() 
 elif deep == "0":
     restartprogram()
 else:
        print_slow(colored("ERROR: AI GRESIT COMANDA BAIATU.? =]]]", 'red'))
        os.system("clear")
        restartprogram() 

def Youtube():
 os.system("clear")
 print(colored("""
  ===========================================================
 .##....##..#######..##.....##.########.##.....##.########..########
  ..##..##..##.....##.##.....##....##....##.....##.##.....##.##......
  ...####...##.....##.##.....##....##....##.....##.##.....##.##......
  ....##....##.....##.##.....##....##....##.....##.########..######..
  ....##....##.....##.##.....##....##....##.....##.##.....##.##......
  ....##....##.....##.##.....##....##....##.....##.##.....##.##......
  ....##.....#######...#######.....##.....#######..########..########
 The YouTubers are work for you
  Every Time ok thats not greate slogan :-[^_^
 ===========================================================
 1. BuToI
 2. Pankea Music
 ==================================================
 7. Exit
 ==================================================
 """, "red"))
 
 yt = raw_input("BUG > ")
 
 if yt == "1":
 	gt330()
 elif yt == "2":
 	h4us()
 elif yt == "3":
 	tzi()
 elif yt == "4":
 	mt()
 elif yt == "5":
     kabu()
 elif yt == "6":
     at()
 elif yt == "7":
     os.system("clear")
     restartprogram() 
 elif deep == "0":
     restartprogram()
 else:
        print_slow(colored("ERROR: AI GRESIT COMANDA BAIATU.? =]]]", 'red'))
        os.system("clear")
        restartprogram() 



def gt330():
	os.system("termux-open-url https://www.youtube.com/channel/UCdlisR7Q5VjNZuiNTpkIwUQ")
	
def h4us():
	os.system("termux-open-url https://www.youtube.com/channel/UCEgWOo3hllLzy8EFmEAsjwA")
	
def fish():
	print_slow(colored("i am searching the sites\nso be patiens.......", 'green'))
 
backtomenubanner = """
BACK TO MENU ?
[1] YES
[2]  NO"""

def restartprogram():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()
	
def backtomenu():
	print backtomenubanner
	backtomenu = raw_input("BUG > ")
	if backtomenu == "1":
		restartprogram()
	elif backtomenu == "2":
		sys.exit()
	else:
		print (colored("ERROR: AI GRESIT COMANDA BAIATU.? =]]]", 'red'))
		time.sleep(2)
		restartprogram()

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
