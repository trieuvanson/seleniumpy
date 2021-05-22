import urllib.request
import re
keywords ="anhyeuem"
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + keywords)
video = re.findall(r"watch\?v=(\S{11})", html.read().decode())
for i in range(10): print(video[i])