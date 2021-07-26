import os , sys	
print("\033[0;36m")
print(''' 
░█████╗░░█████╗░███╗░░██╗██╗░░░██╗███████╗██████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗████╗░██║██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝██║░░██║██╔██╗██║╚██╗░██╔╝█████╗░░██████╔╝░░░██║░░░██║░░██║██████╔╝
██║░░██╗██║░░██║██║╚████║░╚████╔╝░██╔══╝░░██╔══██╗░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝╚█████╔╝██║░╚███║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝ ''')
print("Version: 2.0")
print("New version is coming soon")
print("\033[0;34m")
print("𝗖𝗼𝗱𝗲𝗱 𝗯𝘆 𝗠𝗱 𝗡𝗮𝘇𝗶𝗺")
print("From Bangladesh")
print("Contact me: mdnazim200321@gmail.com")
print("Contact me: https://www.facebook.com/profile.php?id=100068819933855")

print("\033[0;31m")
print(''' 𝗪𝗵𝗮𝘁 𝗱𝗼 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁❓❓❓  ''')
print("\n")
print("\033[0;35m")
print("1.Integer number to Binary number")
print("2.Integer number to Octal number")
print("3.Integer number to Hexadecimal")
print("4.Farenheit to Celsius")
print("5.Celsius to Farenheit")
print("6.Kelvin to Celsius")
print("7.Celsius to Kelvin")
print("8.Kelvin to Farenheit")
print("9.Farenheit to Kelvin")
print("10.Kilometer to Meter")
print("11.Meter to Kilometer")
print("12.Kilometer to Mile")
print("13.Mile to Kilomete")
print("14.Inch to Foot")
print("15.Foot to Inch")
print("16.Meter to Centimete")
print("17.Centimeter to Meter")
print("18.Kilometer to Nautical Mile")
print("19.Nautical mile to Kilometer")
print("\n")
print("\033[0;36m")
num = int(input("Enter any number to continue: "))
print()
# decimal to binary
if num == 1:
	var = int(input("Enter your integer number: "))
	var2 = bin(var)
	print()
	print("~~~~~~~~~~~~~")
	print("Your binary number is" , var2)
	print("~~~~~~~~~~~~~~~")

# decimal to octal
elif num == 2:
	var3 = int(input("Enter your integer number: "))
	var4 = oct(var3)
	print()
	print("~~~~~~~~~~~~~")
	print("Your Octal number is" , var4)
	print("~~~~~~~~~~~~~")
# integer to hexadecimal
elif num == 3:
	var5 = int(input("Enter your integer number: "))
	ver6 = hex(var5)
	print()
	print("~~~~~~~~~~~~~~~~~~")
	print("Your hexadecimal number is" , ver6)
	print("~~~~~~~~~~~~~~~~~~~")
elif num == 4:
      F_num = float(input("Enter your Farenheit num: "))
      Cel = 5/9 * ( F_num - 32 )
      print("Your Celsius number is" , Cel)
elif num == 5:
	Cel_num = float(input("Enter your Celsius num: "))
	Ft_num = (((9 * Cel_num) / 5) + 32)
	print("Your Farenheit number is" , Ft_num)
elif num == 6:
	Calvin = float(input("Enter your calvin number: "))
	CelNum = (Calvin - 273.15)
	print("Your celsius number is" , CelNum)
elif num == 7:
	Celsius = float(input("Enter your celsius number: "))
	Cal = (Celsius + 273.15)
	print("Your Calvin number is" , Cal)
elif num == 8:
	kalvin_num = float(input("Enter you kalvin number: "))
	FarenHeit = (((9 * kalvin_num) - 2298.15)/5)
	print("Your Farenheit Number is" , FarenHeit)
elif num == 9:
	farenHeit = float(input("Enter your Farenheit number: "))
	kalvin_NuM = (((5 * farenHeit) + 2298.35) / 9)
	print("Your kavin number is" , kalvin_NuM)
elif num == 10:
      km = float(input("Enter your kilometer number: "))
      meter = km * 1000
      print(meter , "meter")
elif num == 11:
      met = float(input("Enter your meter number: "))
      kilo = met / 1000
      print(kilo , "kilometer")
elif num == 12:
	kilom = float(input("Enter your kilometer number: "))
	mile = kilom * 0.621371
	print(mile , "mile")
elif num == 13:
	mil = float(input("Enter your mile number: "))
	kil = mil / 0.621371
	print(kil , "Kilometer")
elif num == 14:
	inch = float(input("Enter your inch number: "))
	foot = inch * 0.0833333
	print(foot , "foot")
elif num == 15:
	ft = float(input("Enter your foot number: "))
	incH = ft / 0.0833333
	print(incH , "Inch")
elif num == 16:
      mt = float(input("Enter your meter number: "))
      centimeter = mt * 100
      print(centimeter , "centimeter")
elif num == 17:
	centi = float(input("Enter your centimeter number: "))
	met = centi / 100
	print(met , "meter")
elif num == 18:
	kmeter = float(input("Enter your kilometer number: "))
	nautical_mile = kmeter * 0.539957
	print(nautical_mile , "nautical mile")
elif num == 19:
	nmile = float(input("Enter your Nautical mile number: "))
	kiloMeter = nmile / 0.539957
	print(kiloMeter , 'Kilometer')
else:
	print("••••••••••••••••••••")
	print("Sorry type error")
	print("•••••••••••••••••••")

print("\n")	
question = print("Do you want to update it?")
print()
ask = input("Type yes or no: ")
if ask == "yes":
	os.system("bash update.sh")
else:
	print("Try next time")
