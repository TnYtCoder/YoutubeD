from colorama import Fore , Back , Style
import time as t

print("")
t.sleep(2)
print(Fore.GREEN + "┏┓╋╋┏┓╋╋╋╋┏┓╋╋╋┏┓╋╋╋╋╋┏━━━┓")
t.sleep(0.1)
print("┃┗┓┏┛┃╋╋╋┏┛┗┓╋╋┃┃╋╋╋╋╋┗┓┏┓┃")
t.sleep(0.1)
print("┗┓┗┛┏┻━┳┓┣┓┏╋┓┏┫┗━┳━━┓╋┃┃┃┃")
t.sleep(0.1)
print("╋┗┓┏┫┏┓┃┃┃┃┃┃┃┃┃┏┓┃┃━┫╋┃┃┃┃")
t.sleep(0.1)
print("╋╋┃┃┃┗┛┃┗┛┃┗┫┗┛┃┗┛┃┃━┫┏┛┗┛┃")
t.sleep(0.1)
print("╋╋┗┛┗━━┻━━┻━┻━━┻━━┻━━┛┗━━━┛")
t.sleep(0.1)
print("")
print("[+]  𝘼𝙪𝙩𝙝𝙤𝙧 : 𝙏𝙣𝙔𝙩𝘾𝙤𝙙𝙚𝙧")
print("")
print("")
t.sleep(1)
# Asking User For Url

yt_url = input("[>]  Pᴀsᴛᴇ Tʜᴇ Vɪᴅᴇᴏ URL -->  ")
yt_quality = input("[>]  Eɴᴛᴇʀ ʏᴏᴜʀ ᴏ̨ᴜᴀʟɪᴛʏ (ᴍᴇᴅɪᴜᴍ / ʜᴅ720 / ʜᴅ1080) -->  ")

# Turning The Input Into File

n = "video"
q = '"'
x = " -q "
s = " "
y = ".mp4"

f = open("video.sh" , "w+")
f.write("youtubedr download -o " + str(q) + str(n) + str(q) + str(y) + str(x) + str(yt_quality) + str(s) + str(yt_url))
f.close()
