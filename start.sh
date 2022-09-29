#!bin/bash
clear
PS0='results:\n'
$PS1="\[\e[0;96m\]command\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\]"
echo "Type \033[96m Type enter to start:[0m"
read useri
python brutezip.py
