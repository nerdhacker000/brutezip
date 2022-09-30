import zipfile
from zipfile import ZipFile
print( str("\033[94m		BRUTEZIP was made by Nerd Haka")) 
print( str("\033[96m	Find more tools and tutorials: www.nerdhaka.blogspot.com")) 

print( str("----------------------------------------------------------")) 
print( str("¦ Tool Command    ¦ Description				 ¦")) 
print( str("¦\033[94m brute test.zip  ¦ test.zip is the locked file ¦")) 
print( str("¦ default.attack  ¦ Attack using default wordlist	 ¦")) 
print( str("-----------------------------------------------------------")) 

def brute_password(wordlist, obj):
    idl = 0
    with open(wordlist, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    idl += 1
                    obj.extractall(pwd=word)
                    print("Password found at line", idl)
                    print("Password is", word.decode())
                    return True
                except:
                    continue
    return False

inputfile=input("Enter command to process:  ")
inputfile=inputfile.replace("brute ","")
inputkey=input("If you don't know what to type, Type: default.attack\nAttack using: ")
wordlist = inputkey
zip_file = inputfile
obj = zipfile.ZipFile(zip_file)
cnt = len(list(open(wordlist, "rb")))
#print("There are total", cnt, "number of attempts")

if brute_password(wordlist, obj) == False:
    print("Password not found in the wordlist, update your default.attack try a different wordlist")
