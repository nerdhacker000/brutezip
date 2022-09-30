#!bin/bash
clear
echo "▉▒▒▒╮ 	 ▉▒▒▓╮  ╮     ╭ ▉▒▒▒▒▒▓  ▉▒▒▒▒▓  ▉▒▒▒▒▓╮   ▉  ▉▒▒▒▒▓╮"
echo "▉    ▓  ▉    ▓  ▉     ▉    ▓     ▉             ╭▒  ▉  ▉     ▉"
echo "▉▒▒▒▒╯╮ ▉▒▒▒▒╮  ▉     ▉    ▓     ▉▒▒▒▒▓     ╭▒     ▉  ▉▒▒▒▒▓╯"
echo "▉       ▓     ▉ ▓     ▉    ▉     ▓        ╭▒       ▉  ▉    "
echo "▉▒▒▒▒▒╯ ▉     ▓  ╰▒▒▒╯     ▓     ▉▒▒▒▒▓  ▉▒▒▒▒▒▓   ▉  ▉"
PS0='results:\n'
PS1="\[\e[0;96m\]command\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\]"
echo "Press enter to start:"
read useri
python brutezip.py
