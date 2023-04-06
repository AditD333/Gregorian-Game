import calendar as c
import os,sys
from random import randint as rand
import time
import datetime as dt
import platform
from functools import lru_cache
from inputimeout import inputimeout
plat = platform.system()
a,b = os.get_terminal_size()





























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































lru_cache(None)
def clear():
	if plat == 'Windows':
		os.system('cls')
	else:
		os.system('clear')

clear()

if sys.version_info[0] < 3:
	print("Error! Please use Python 3 and above!")
	sys.exit()
elif sys.version_info[0] == 3:
		if sys.version_info[1] >= 11:
			sys.set_int_max_str_digits(0)
		elif 7 <= sys.version_info[1] <= 9:
			if sys.version_info[2] >= 14:
				sys.set_int_max_str_digits(0)
		elif sys.version_info[1] == 10:
			if sys.version_info[2] >= 7:
				sys.set_int_max_str_digits(0)
		else:
			pass
elif sys.version_info[0] >= 4:
	sys.set_int_max_str_digits(0)


clear()



def menu(record,r_name):
	modeA = ""
	while modeA.isnumeric() is False or (ord(modeA) < 49 or ord(modeA) > 50) or modeA == "" or len(modeA) != 1:
		clear()
		print("-"*a)
		print("\n\nWELCOME TO GREGORIAN GAME!!!")
		print("\n\n")
		print("Select the type!\n\n")
		print("1. Game Start!\n")
		print("2. Recent Plays\n")
		print("\n\nUse Ctrl+C or Control+C to instantly exit the program")
		print("\n\n")
		print("-"*a)
		modeA = input("\n\n\nSelect your play mode >>>  ")

	if modeA == "1":
		digits_decide_low = ""
		digits_decide_high = ""
		while digits_decide_low.isnumeric() is False or digits_decide_high.isnumeric() is False or digits_decide_low == "0" or digits_decide_high == "0": 
			clear()
			print("Enter number of digits at least 1 (one) to generate calendar questions!")
			digits_decide_low = input("\n\nEnter least number of digit(s) --->  ")
			digits_decide_high = input("\n\nEnter most number of digit(s) --->  ")
		dL = int(digits_decide_low)
		dH = int(digits_decide_high)
		if dL > dH:
			clear()
			print("Error! the least digits is more than the highest!")
			x14 = input("\n\nBack to main menu!")
			clear()
			menu(record,r_name)
		pts = 0
		lives = 3

		clear()
		print("Game will start, read the instruction below!\n\n")
		print("1. Guess the day of the week IN 16 SECONDS that corresponds to question! Only the first 3 letter(s)! (Case INSENSITIVE)")
		print("2. You have 3 life(s)/attempt(s) to try, accumulated until next question(s)")
		print("3. The calendar is in GREGORIAN CALENDAR format! Including +1752 and below (!)")
		print("4. (For some cases only) Watch out! One backspace when try to solve the answer moves the field by one line!")
		print("5. Wait UNTIL the next question to input another answer, otherwise POTENTIAL TO BE WRONG INSTANTLY!")
		print("\nSpecial notes: If you play with 1 - 4 digit mode, it will be forced to positive-signed 4-digit format")
		print("\n1-digit = (From Dec 26th [Or 12 - 26] of) -0001 - +0009 \n\n2-digit = +0010 - +0099\n\n3-digit = +0100 - +0999\n\nWhile the rest is proper 4-digit = +1000 - +9999")
		x10 = input("\n\nGOOD LUCK!! Enter to start!")
		clear()
		while lives != 0:
			year = rand(dL,dH)
			d = '0123456789'
			e = []
			y_indicate = []
			for h in d:
				e.append(h)
			for random in range(0,year):
				y_indicate.append(e[rand(0,9)])
			
			if year > 1:
				if year < 4:
					if year == 3:
						if y_indicate[0] == "0":
							y_indicate[0] = "1"
						y_indicate.insert(0, '0')
					elif year == 2:
						if y_indicate[0] == "0":
							y_indicate[0] = "1"
						y_indicate.insert(0, '0')
						y_indicate.insert(0, '0')
						
				elif year >= 4:
					if y_indicate[0] == "0":
						y_indicate[0] = "1"

				y1 = "".join(y_indicate)
				y = int(y1)
				y400 = y%400
				month = rand(1,12)
				if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
					d = rand(1,31)
				elif month == 4 or month == 6 or month == 9 or month == 11:
					d = rand(1,30)
				elif month == 2:
					if (y400%4 == 0 and y400%100 == 0 and y400%400 == 0):
						d = rand(1,29)
					elif y400%4 == 0 and y400%100 == 0 and y400%400 != 0:
						d = rand(1,28)
					elif y400%4 == 0 and y400%100 != 0 and y400%400 != 0:
						d = rand(1,29)
					elif y400%4 != 0:
						d = rand(1,28)
				print("+%s - %02d - %02d" % (y1,month,d))
				try:
					ans = inputimeout(prompt="\n\nAnswer -->  ",timeout=16)
					if ans.lower() == c.day_abbr[c.weekday(y400,month,d)].lower():
						pts = pts + year
						print("\n\nCorrect!")
						time.sleep(2)
					else:
						lives = lives - 1
						print("\nWrong! The answer must be [%s]" % (c.day_abbr[c.weekday(y400,month,d)]))
						print("\n\nYou have %s life(s) left!" % (lives))
						time.sleep(3)
				except Exception:
					lives = lives - 1
					print("\nTime's Out! The answer is [%s]" % (c.day_abbr[c.weekday(y400,month,d)]))
					print("\n\nYou have %s life(s) left!" % (lives))
					time.sleep(3)
				clear()

			elif year == 1:
				y = rand(-1,9)
				if y == -1:
					month = 12
					d = rand(26,31)
					print("%05d - %02d - %02d" % (y,month,d))
					try:
						ans = inputimeout(prompt="\n\nAnswer -->  ",timeout=16)
						if ans.lower() == c.day_abbr[c.weekday(y,month,d)].lower():
							pts = pts + year
							print("\n\nCorrect!")
							time.sleep(2)
						else:
							lives = lives - 1
							print("\nWrong! The answer must be [%s]" % (c.day_abbr[c.weekday(y,month,d)]))
							print("\n\nYou have %s life(s) left!" % (lives))
							time.sleep(3)
					except Exception:
						lives = lives - 1
						print("\nTime's Out! The answer is [%s]" % (c.day_abbr[c.weekday(y,month,d)]))
						print("\n\nYou have %s life(s) left!" % (lives))
						time.sleep(3)
					clear()
				elif y >= 0 and y <= 9:
					month = rand(1,12)
					if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
						d = rand(1,31)
					elif month == 4 or month == 6 or month == 9 or month == 11:
						d = rand(1,30)
					elif month == 2:
						if (y%4 == 0 and y%100 == 0 and y%400 == 0):
							d = rand(1,29)
						elif y%4 == 0 and y%100 == 0 and y%400 != 0:
							d = rand(1,28)
						elif y%4 == 0 and y%100 != 0 and y%400 != 0:
							d = rand(1,29)
						elif y%4 != 0:
							d = rand(1,28)
					print("+%04d - %02d - %02d" % (y,month,d))
					try:
						ans = inputimeout(prompt="\n\nAnswer -->  ",timeout=16)
						if ans.lower() == c.day_abbr[c.weekday(y,month,d)].lower():
							pts = pts + year
							print("\n\nCorrect!")
							time.sleep(2)
						else:
							lives = lives - 1
							print("\nWrong! The answer must be [%s]" % (c.day_abbr[c.weekday(y,month,d)]))
							print("\n\nYou have %s life(s) left!" % (lives))
							time.sleep(3)
					except Exception:
						lives = lives - 1
						print("\nTime's Out! The answer is [%s]" % (c.day_abbr[c.weekday(y,month,d)]))
						print("\n\nYou have %s life(s) left!" % (lives))
						time.sleep(3)
					clear()



		record.append(pts)
		name = ""
		while len(name) == 0:
			clear()
			print("Game Over! You have %s point(s)!!\n\n" % (pts))
			name = input("Enter name -->  ")
		r_name.append(name)
		print("\n\n")
		x11 = input("\n\nEnter to continue to main menu!")
		menu(record,r_name)



	elif modeA == "2":
		clear()
		if len(record) == 0 and len(r_name) == 0:
			print("No score(s) here! Try to play the game first! :):)\n")
			x12 = input("\n\nEnter to continue to main menu!")
			clear()
			menu(record,r_name)
		total = 0
		print("-"*a)
		for x in range (0,len(record)):
			print("%s.\t%s   = \t%s point(s)\n" % (x+1,r_name[x],record[x]))
		print("-"*a)
		print("\n\nHighest point(s) this session  =  %s\n\n" % (max(record)))
		for s in range (0,len(record)):
			total = total + record[s]
		print("Total point(s) this session  =  %s\n\n" % (total))
		print("Average point(s) this session = %s (rem %s)\n\n" % (total//len(record),total%(len(record))))
		x13 = input("\n\nEnter to continue to main menu!")
		clear()
		menu(record,r_name)


	elif modeA == "0":
		clear()
		menu(record,r_name)

	else:
		pass




record = []
r_name = []
try:
	menu(record,r_name)
except KeyboardInterrupt:
	try:
		clear()
		print("SEE YOU SOON!!\n\n")
		print("\n\n\n©+2023 GREGORIAN GAME by HeptaVerdixx")
		time.sleep(5)
		clear()
		sys.exit()
	except KeyboardInterrupt:
		clear()
		sys.exit()
