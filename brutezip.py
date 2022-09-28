import zipfile
from colorama import Fore
print('\033[31m' + '010101010101010101010101111001101111011110011010101100111100001110110010101')
print('\033[31m' + '1  __________ ____        ____  ____      _    ____ _  _______ ______     1')
print('\033[31m' + '0 / /__  /_ _|  _ \      /  ___ |  _ \   / \  / ___| |/ / ____|  _ \ \    0')
print('\033[31m' + '0 | |  / / | || |_) |____| |   | |_) |  / _ \| |   |  /|  _| | |_) | |    1')
print('\033[31m' + '1 | |  / /_| ||  __/_____| |___|  _ <  / ___ \ |___| . \| |__|  _ || |< > 0')
print('\033[31m' + '1 | |/____|___|_|         \____|_| \_\/_/   \_\____|_|\_\_____|_| \_\|    0')
print('\033[31m' + '0 \_\                                                             /_/     1')
print('\033[31m' + '1               Zip File Password Cracking Tool	                      1')
print('\033[31m' + '0                    Coded by: Goatherd#9951                              0')
print('\033[31m' + '0                github:https://github.com/G0atherd                       1')
print('\033[31m' + '1									      0')
print('\033[31m' + '010101010101010101010101111001101111011110011010101100111100001110110010110')

print("\033[36")
file = str(input("Please inpute your zip file:"))
wordlist1 = str(input("Please inpute your wordlist:"))

def main():
	"""
	Zipfile password cracker using a brute-force dictionary attack.
	"""
	zipfilename = file
	dictionary = wordlist1

	password = None
	zip_file = zipfile.ZipFile(zipfilename)
	with open(dictionary, 'r') as f:
		for line in f.readlines():
			password = line.strip('\n')
			try:
				zip_file.extractall(pwd=password)
				password = 'Password found: %s' % password
			except:
				pass
	print("Password:"+ password)

if __name__ == '__main__':
	main()
