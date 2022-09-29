import zipfile
from zipfile import ZipFile

PS1="\033[96m(Choose)->\033[0m"
print( "\033[94m	
print( "\033[94m	 ____	 ____   _       _ ______   ______  ______  ______  ______"
print( "\033[94m	||   \\ ||   \\ \\     //|__  __|||______||___ /  |__  __||	 \" 
print( "\033[94m	||___// ||___// ||     ||   ||	 ||______    //	     ||	  | _____/" 
print( "\033[94m	||    \\||    \\||     ||   ||	 ||______| _//___  __||__ ||" 
print( "\033[94m	||____//||    ||\\_____//   ||	 \\_______|______||______|||"
print( "\033[94m	\______/\______/ \______/\______/ \______/\______/\______/\______/"
print( "\033[94m		BRUTEZIP was made by Nerd Haka"
print( "\033[96m	        Find more tools and tutorials: www.nerdhaka.blogspot.com"

print( "----------------------------------------------------------") 
print( "¦ Tool Command    ¦ Description				 ¦") 
print( "¦ \033[94m brute test.zip  ¦ test.zip is the locked file ¦") 
print( "¦ default attack  ¦ Attack using default wordlist	 ¦") 
print( "-----------------------------------------------------------") 

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

inputfile=input("Enter command to process")
inputfile=inputfile.replace("brute ","")
inputkey=input("Attack Using? If you don't know what to type, Type: default.attack")
wordlist = inputkey
zip_file = inputfile
obj = zipfile.ZipFile(zip_file)
cnt = len(list(open(wordlist, "rb")))
#print("There are total", cnt, "number of attempts")

if crack_password(wordlist, obj) == False:
    print("Password not found in the wordlist, try a different wordlist")
