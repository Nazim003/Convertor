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
      
	
else:
	print("••••••••••••••••••••")
	print("Sorry type error")
	print("•••••••••••••••••••")






