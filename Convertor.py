print("\033[0;36m")
print(''' 
░█████╗░░█████╗░███╗░░██╗██╗░░░██╗███████╗██████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗████╗░██║██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝██║░░██║██╔██╗██║╚██╗░██╔╝█████╗░░██████╔╝░░░██║░░░██║░░██║██████╔╝
██║░░██╗██║░░██║██║╚████║░╚████╔╝░██╔══╝░░██╔══██╗░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝╚█████╔╝██║░╚███║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝ ''')

print("\033[0;34m")
print("𝗖𝗼𝗱𝗲𝗱 𝗯𝘆 𝗠𝗱 𝗡𝗮𝘇𝗶𝗺")
print("From Bangladesh")

print("\033[0;31m")
print(''' 𝗪𝗵𝗮𝘁 𝗱𝗼 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁❓❓❓  ''')
print("\n")
print("\033[0;35m")
print("1.Integer number to Binary number")
print("2.Integer number to Octal number")
print("3.Integer number to Hexadecimal")
print("4.Farenheit to Celsius")
print("5.Celsius to Farenheit")
print("6.Kalvin to Celsius")
print("7.Celsius to Kalvin")
print("8.Kalvin to Farenheit")
print("9.Farenheit to Kalvin")
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
else:
	print("••••••••••••••••••••")
	print("Sorry type error")
	print("•••••••••••••••••••")






