#  _____  __   ___    ___         _
# |_   _| \ \ / / |_ / __|___  __| |___ _ _
#   | || ' \ V /|  _| (__/ _ \/ _` / -_) '_|
#   |_||_||_|_|  \__|\___\___/\__,_\___|_|

#import
import time, os, subprocess, sys

#req

time.sleep(0.5)
os.system('clear')
time.sleep(0.5)

class fg:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

def typewriter(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()

#logo

def logo():
	logo = '''

\033[32m   _____           _        _ _       _   _
   \_   \_ __  ___| |_ __ _| | | __ _| |_(_) ___  _ ___
    / /\/ '_ \/ __| __/ _` | | |/ _` | __| |/ _ \| '_  |
 /\/ /_ | | | \__ \ || (_| | | | (_| | |_| | (_) | | | |
 \____/ |_| |_|___/\__\__,_|_|_|\__,_|\__|_|\___/|_| |_|
 <----------------------------------------------------->
 | Github : TnYtCoder |       ____       _             |
 | Setup Installation |        /  (__/_// )  _/_ _     |
 | Star On Github ; ) |       (/)  /  /(__()(/(-/      |
 +-----------------------------------------------------+

	'''
	typewriter(logo)

logo()

time.sleep(2)

print("\033[35m Installing Requirements\n")

time.sleep(2)
requests = "requests"
pkg = "youtubedr"

try:
	print("\033[34m Please Wait...")
	subprocess.run(["pip", "install", requests], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
	subprocess.run(["pkg", "install", pkg], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

except:
	print("\033[31m Error\n")
	sys.exit()

time.sleep(1)
print("\n\033[32m Installation Done !")
time.sleep(1)
