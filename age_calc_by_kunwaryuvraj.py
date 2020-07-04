"""

Originally created by =>  K U N W A R  Y U V R A J 
Owner's site => https://KunwarYuvraj.herokuapp.com

*** If you are copying this, Please understand logic first, Then you can customize it ;) ***

Source code is uploaded on my github :)

"""

import datetime as dt 

def age_calc(user_year, user_month, user_day):
	if user_year % 4 == 0:
		if user_year % 100 == 0:
			if user_year % 400 == 0:
				month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
			else:
				month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		else:
			month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	else:
		month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	user_dob = dt.datetime(user_year, user_month, user_day)
	current_year = dt.datetime.now().year
	current_month = dt.datetime.today().month
	current_day = dt.datetime.today().day

	if user_day > current_day: 
		current_month -= 1
		current_day += month[user_month-1] 

	if user_month > current_month:
		current_year -= 1
		current_month += 12

	user_age_year = current_year - user_year 
	user_age_month = current_month - user_month
	user_age_day = current_day - user_day

	total_seconds = user_age_year*31536000 + user_age_month*2628002.88 + user_age_day*86400

	if user_age_year < 0:
		message = f'\nHOLD UP..\nYou are not born yet !\nWhat are you doing here ?'
		return message
	else:
		message = f'\nYou are {user_age_year} years, {abs(user_age_month)} months and {user_age_day} days old !\n\nFUN FACT\nYou have spended a total of {total_seconds} seconds, {total_seconds/60} minutes and {total_seconds/(60*60)} hours !'
		return message

user_year = int(input("Enter year: "))
user_month = int(input('Enter month: '))
user_day = int(input('Enter day: '))

print(age_calc(user_year, user_month, user_day))