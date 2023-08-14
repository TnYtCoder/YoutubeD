#import
import os, sys, time, subprocess

#req
time.sleep(0.5)
os.system('clear')
time.sleep(0.5)

def is_termux_package_installed(package_name):
    try:
        result = subprocess.run(["pkg", "list-installed", package_name], capture_output=True, text=True, check=True)
        return package_name in result.stdout
    except subprocess.CalledProcessError:
        return False

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

#installation verification

package_to_check = "youtubedr"

if is_termux_package_installed(package_to_check):
    print(" ")
else:
    print("\033[31m Please Install Requirements")
    sys.exit()

#logo
def logo():
	logo = '''
\033[32m _____.___.              __       ___.          ________
 \__  |   | ____  __ ___/  |_ __ _\_ |__   ____ \______ \ 
  /   |   |/  _ \|  |  \   __\  |  \ __ \_/ __ \ |    |  \ 
  \____   (  <_> )  |  /|  | |  |  / \_\ \  ___/ |    `   \ 
  / ______|\____/|____/ |__| |____/|___  /\___  >_______  /
  \/                                   \/     \/        \/
 <- -----------------------------------  -----  --------  ->
 | Github : TnYtCoder                                      |
 | Python Script To Download Youtube Video At High Quality |
 +---------------------------------------------------------+
	'''
	typewriter(logo)

logo()

time.sleep(1)
url = input("\n\033[33m Enter Url : ")
name = input("\033[33m Enter File Name  (exclude .mp4) : ")
command = "youtubedr download -o '{}'.mp4 -q 18 {}".format(name, url)

try:
	print("\n\033[34m Processing...")
	subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except:
	print("\n\033[31m Error ?!")
	print(" Please Check Your Internet Connection")

print("\n\033[32m Task Completed !!")

time.sleep(1)
